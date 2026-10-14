"""Contratos do verificador, com pontuação sintética e sintaxe técnica."""

import unittest
from check_language import issues


class LanguageTests(unittest.TestCase):
    def test_markdown_prose_and_authored_examples_are_checked(self):
        self.assertEqual(len(issues("Título \u2014 exemplo\n```text\nTexto \u2013 autoral\n```", ".md")), 2)

    def test_technical_code_and_link_targets_are_not_prose(self):
        self.assertEqual(issues("`x \u2013 y`\n```js\nx --;\nconst fixture = '\u2014';\n```\n[Nome](https://example.org/a\u2013b)", ".md"), [])

    def test_link_labels_remain_authored(self):
        self.assertEqual(len(issues("[Texto \u2014 exemplo](arquivo.md)", ".md")), 1)

    def test_shorter_fence_does_not_end_technical_example(self):
        sample = "````js\n```\nconst fixture = '\u2014';\n```\n````"
        self.assertEqual(issues(sample, ".md"), [])

    def test_html_visible_text_entities_and_attributes(self):
        sample = '<h1>VÃO &mdash; arquitetura</h1><img alt="Conceito \u2013 casa"><script>value--;</script>'
        self.assertEqual(len(issues(sample, ".html")), 2)

    def test_javascript_feedback_is_checked_but_operators_are_not(self):
        sample = 'value--; const pattern = /[\u2013\u2014]/; status.textContent = "Pronto \\u2014 confira";'
        self.assertEqual(len(issues(sample, ".js")), 1)

    def test_css_generated_copy_is_checked(self):
        self.assertEqual(len(issues('p::before { content: "Texto \u2014 teste"; } a { margin-left: -2px; }', ".css")), 1)

    def test_documented_exception_requires_reason(self):
        self.assertEqual(issues('Nome \u2014 Original <!-- meds-language-exception: nome de terceiro confirmado -->', ".md"), [])
        self.assertEqual(len(issues('Texto \u2014 exemplo <!-- meds-language-exception: -->', ".md")), 1)

    def test_ordinary_punctuation_and_hyphens_are_preserved(self):
        self.assertEqual(issues("Título: arquitetura. Texto claro, com contexto; sem excesso (exemplo). pt-BR", ".md"), [])


if __name__ == "__main__":
    unittest.main()
