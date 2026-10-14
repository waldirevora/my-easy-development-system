"""Confira pontuação autoral em Markdown, HTML, strings JS e content CSS."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re


DASHES = {chr(0x2013), chr(0x2014)}
SUPPORTED = {".md", ".html", ".js", ".cjs", ".css"}


def text_issues(text, line=1):
    return [(line + text[:index].count("\n"), f"U+{ord(char):04X}")
            for index, char in enumerate(text) if char in DASHES]


def exception(line):
    """Exceção pontual e explícita; comentário vazio não libera o conteúdo."""
    return bool(re.search(r"<!-- meds-language-exception:\s*\S.{9,}? -->", line))


class HTMLCopy(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues = []
        self.technical = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "code", "pre"}:
            self.technical += 1
        attrs = dict(attrs)
        for key in ("title", "alt", "aria-label", "placeholder"):
            self.issues.extend(text_issues(attrs.get(key, ""), self.getpos()[0]))
        if tag == "meta" and attrs.get("name") in {"description", "application-name"}:
            self.issues.extend(text_issues(attrs.get("content", ""), self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in {"script", "style", "code", "pre"}:
            self.technical = max(0, self.technical - 1)

    def handle_data(self, data):
        if not self.technical:
            self.issues.extend(text_issues(data, self.getpos()[0]))


def issues(content, suffix):
    if suffix == ".html":
        parser = HTMLCopy()
        parser.feed(content)
        return parser.issues
    if suffix == ".md":
        result = []
        fence = None
        prose_fence = False
        for number, line in enumerate(content.splitlines(), 1):
            match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if match and fence is None:
                fence = match[1]
                prose_fence = match[2].strip().lower() in {"", "md", "markdown", "text"}
                continue
            if (match and fence and fence[0] == match[1][0]
                    and len(match[1]) >= len(fence) and not match[2].strip()):
                fence = None
                continue
            if (fence and not prose_fence) or exception(line):
                continue
            # Inline code e destinos de links são técnicos; rótulos continuam autorais.
            line = re.sub(r"(`+).*?\1", "", line)
            line = re.sub(r"\]\([^)]*\)", "]", line)
            result.extend(text_issues(line, number))
        return result
    if suffix in {".js", ".cjs"}:
        # Scanner lexical proporcional, não AST nem verificador de toda linguagem.
        tokens = re.compile(r'''//[^\n]*|/\*[\s\S]*?\*/|/(?:\\.|[^/\\\n])+/[dgimsuvy]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`''')
        result = []
        for token in tokens.finditer(content):
            raw = token.group()
            if raw[0] not in "\"'`":
                continue
            value = re.sub(r"\\u([0-9a-fA-F]{4})", lambda match: chr(int(match[1], 16)), raw[1:-1])
            result.extend(text_issues(value, content[:token.start()].count("\n") + 1))
        return result
    if suffix == ".css":
        result = []
        for token in re.finditer(r'''\bcontent\s*:\s*(["'])(.*?)\1''', content, re.S):
            result.extend(text_issues(token[2], content[:token.start()].count("\n") + 1))
        return result
    raise ValueError(f"Formato não suportado: {suffix}")


def findings(path):
    return issues(path.read_text(encoding="utf-8"), path.suffix)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    failures = []
    count = 0
    for supplied in args.paths:
        path = supplied.resolve()
        if not path.is_relative_to(root) or path.suffix not in SUPPORTED:
            parser.error("Destino fora do MEDS ou formato não suportado.")
        count += 1
        failures.extend(f"{path.relative_to(root)}:{line}: {code}" for line, code in findings(path))
    if failures:
        print("\n".join(failures))
        return 1
    print(f"PASS: linguagem nas superfícies suportadas de {count} arquivos; revisão editorial permanece necessária.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
