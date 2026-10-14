"""Regressão da preparação em destinos descartáveis dentro do workspace."""

from pathlib import Path
import shutil
import tempfile
import unittest

from check import find_root
from copy_harness import HARNESS_FILES, copy_harness


class CopyHarnessTests(unittest.TestCase):
    def setUp(self):
        root = find_root(Path(__file__))
        self.temporary = tempfile.TemporaryDirectory(prefix=".qa-meds-temporario-", dir=root)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.source = self.base / "Origem com espaços e acentos"
        self.source.mkdir()
        for relative in HARNESS_FILES:
            target = self.source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / relative, target)
        self.destination = self.base / "Projeto fictício"

    def test_copy_without_git_keeps_dependencies_and_governance(self):
        copy_harness(self.source, self.destination)
        files = [p for p in self.destination.rglob("*") if p.is_file()]
        self.assertEqual(len(files), 28)
        self.assertFalse((self.destination / ".git").exists())
        self.assertEqual((self.source / "LICENSE").read_bytes(),
                         (self.destination / "MEDS-LICENSE").read_bytes())
        for relative in HARNESS_FILES:
            if relative not in ("AGENTS.md", "LICENSE"):
                self.assertEqual((self.source / relative).read_bytes(),
                                 (self.destination / relative).read_bytes())
        agents = (self.destination / "AGENTS.md").read_text(encoding="utf-8")
        original = (self.source / "AGENTS.md").read_text(encoding="utf-8")
        self.assertEqual(agents.split("## Regra principal", 1)[1].split(
            "\nAs fontes copiadas", 1)[0], original.split("## Regra principal", 1)[1])
        self.assertIn("aos seus próprios requisitos", agents)
        self.assertIn("Raiz do projeto independente", agents)
        self.assertNotIn("MEDS-WORKSPACE-START", agents)
        self.assertNotIn("criar automaticamente `workspaces/<slug>/`", agents)

    def test_invalid_scope_markers_fail_before_writing(self):
        path = self.source / "AGENTS.md"
        original = path.read_text(encoding="utf-8")
        start = "<!-- MEDS-WORKSPACE-START -->"
        end = "<!-- MEDS-WORKSPACE-END -->"
        variants = [original.replace(start, ""), original.replace(end, ""),
                    original.replace(start, "__START__").replace(end, start).replace("__START__", end)]
        for content in variants:
            with self.subTest(content=content[:60]):
                path.write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Marcadores de escopo"):
                    copy_harness(self.source, self.destination)
                self.assertFalse(self.destination.exists())

    def test_existing_empty_directory_is_supported(self):
        self.destination.mkdir()
        self.assertEqual(copy_harness(self.source, self.destination), self.destination)

    def test_conflicting_project_is_untouched(self):
        self.destination.mkdir()
        original = self.destination / "AGENTS.md"
        original.write_text("Instruções existentes: preservar.\n")
        with self.assertRaisesRegex(ValueError, "Destino ocupado"):
            copy_harness(self.source, self.destination)
        self.assertEqual(original.read_text(), "Instruções existentes: preservar.\n")
        self.assertEqual(list(self.destination.iterdir()), [original])

    def test_missing_dependency_fails_before_writing(self):
        (self.source / "standards/capability-routing-v1.md").unlink()
        with self.assertRaisesRegex(ValueError, "Fonte essencial ausente"):
            copy_harness(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_target_inside_framework_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "fora da instalação"):
            copy_harness(self.source, self.source / "produto")
        self.assertFalse((self.source / "produto").exists())

    def test_symlink_destination_is_rejected(self):
        real = self.base / "Destino real"
        real.mkdir()
        try:
            self.destination.symlink_to(real, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Criação de symlink não disponível neste ambiente.")
        with self.assertRaisesRegex(ValueError, "links simbólicos"):
            copy_harness(self.source, self.destination)
        self.assertEqual(list(real.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
