"""Verificações locais do MEDS, sem dependências externas ou arquivos gerados."""

import argparse
import ast
from pathlib import Path, PureWindowsPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from check_language import findings


def find_root(script_path: Path) -> Path:
    """Suba a partir do arquivo até os dois marcadores, sem consultar cwd."""
    for candidate in script_path.resolve().parents:
        if (candidate / "AGENTS.md").is_file() and (
            candidate / ".agents/skills"
        ).is_dir():
            return candidate
    raise ValueError("Raiz ausente: necessários AGENTS.md e .agents/skills/.")


def validate(root: Path) -> None:
    """Confira estrutura, fontes Python e links/cercas Markdown locais."""
    for name in ("AGENTS.md", "README.md", "LICENSE", "docs/README.md",
                 "docs/GUIA_DE_USO.md", "examples/README.md",
                 "standards/README.md", "templates/README.md",
                 "standards/capability-routing-v1.md", "workspaces/.gitkeep",
                 "codex_lab_5_5/ai_triage.py", "codex_lab_5_5/test_ai_triage.py"):
        if not (root / name).is_file():
            raise ValueError(f"Fonte essencial ausente: {name}")

    standards = set((root / "standards").glob("*.md")) - {
        root / "standards/README.md"
    }
    skills = set((root / ".agents/skills").glob("*/SKILL.md"))
    templates = set((root / "templates").glob("*.md")) - {
        root / "templates/README.md"
    }
    if (len(standards), len(skills), len(templates)) != (7, 12, 5):
        raise ValueError("Inventário diferente de 7 Standards / 12 Skills / 5 templates.")

    # Projetos locais não pertencem à validação das fontes do framework.
    workspace = root / "workspaces"
    if workspace.is_symlink() or workspace.resolve() != root / "workspaces":
        raise ValueError("workspaces deve permanecer dentro da raiz MEDS.")
    marker = workspace / ".gitkeep"
    if marker.is_symlink() or marker.resolve() != workspace / ".gitkeep":
        raise ValueError("Marcador workspaces/.gitkeep externo à raiz.")

    sources = {root / "AGENTS.md", root / "README.md"}
    for directory in ("standards", "templates", "docs", "examples",
                      ".agents/skills", "codex_lab_5_5", "scripts"):
        base = root / directory
        if base.is_symlink() or not base.resolve().is_relative_to(root):
            raise ValueError(f"Diretório fora da raiz: {directory}")
        sources.update(base.rglob("*.md"))
        sources.update(base.rglob("*.py"))

    links = 0
    markdown_count = 0
    python_count = 0
    for path in sorted(sources):
        relative = path.relative_to(root)
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Fonte fora da raiz: {relative}")
        content = path.read_text(encoding="utf-8")
        if path.suffix == ".py":
            ast.parse(content, filename=str(relative))
            python_count += 1
            continue
        markdown_count += 1
        language = findings(path)
        if language:
            raise ValueError(f"Pontuação autoral em {relative}: {language}")
        if path in skills:
            frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
            if not frontmatter:
                raise ValueError(f"Frontmatter ausente: {relative}")
            fields = dict(re.findall(r"^(name|description):\s*(.+)$",
                                     frontmatter[1], re.M))
            if fields.get("name", "").strip("\"'") != path.parent.name or not (
                fields.get("description", "").strip("\"'")
            ):
                raise ValueError(f"Nome/descrição inválidos: {relative}")

        fence = None
        prose = []
        for line in content.splitlines():
            match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if match and fence is None:
                fence = match[1]
            elif match and fence and match[1][0] == fence[0] and (
                len(match[1]) >= len(fence) and not match[2].strip()
            ):
                fence = None
            elif fence is None:
                prose.append(line)
        if fence:
            raise ValueError(f"Cerca Markdown sem fechamento: {relative}")

        # Os documentos usam links inline; não testar URLs externas nem âncoras.
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", "\n".join(prose)):
            target = target.strip().strip("<>")
            windows = PureWindowsPath(target)
            if windows.drive or windows.is_absolute() or target.startswith("/"):
                raise ValueError(f"Link interno absoluto: {relative}")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                raise ValueError(f"Link interno ausente/externo: {relative}: {target}")
            links += 1

    print("PASS: 7 Standards / 12 Skills / 5 templates.")
    print(f"PASS: {python_count} fontes Python; {markdown_count} Markdown; "
          f"{links} destinos de links internos; frontmatter e cercas.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-tests", action="store_true",
                        help="Executar somente as verificações estáticas.")
    args = parser.parse_args()
    try:
        root = find_root(Path(__file__))
        print(f"Raiz descoberta: {root}", flush=True)
        validate(root)
    except (OSError, ValueError, SyntaxError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if args.skip_tests:
        print("Suíte Python não executada (--skip-tests).")
        return 0
    sys.stdout.flush()
    for directory in ("codex_lab_5_5", "scripts"):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "unittest", "discover", "-s",
             directory, "-p", "test_*.py", "-v"], cwd=root, check=False
        )
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
