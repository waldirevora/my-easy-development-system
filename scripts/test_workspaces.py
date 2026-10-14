"""Contratos de workspaces e Git; fixtures locais, sem alterar o índice."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from check import find_root, validate


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.root = find_root(Path(__file__))
        self.workspace = self.root / "workspaces"
        # Verificar resolução antes de qualquer escrita de fixture.
        self.assertEqual(self.workspace.resolve(), self.root / "workspaces")
        self.assertTrue((self.workspace / ".gitkeep").is_file())

    def git(self, *args):
        if not shutil.which("git") or not (self.root / ".git").exists():
            self.skipTest("Git/checkout ausente; testes Git não executados.")
        return subprocess.run(["git", *args], cwd=self.root, check=False,
                              capture_output=True, text=True, encoding="utf-8")

    def test_git_ignores_project_files_at_all_depths(self):
        paths = ["workspaces/projeto-qa/index.html",
                 "workspaces/projeto-qa/assets/imagem.svg",
                 "workspaces/projeto-qa/.gitkeep",
                 "workspaces/projeto-qa/.env.example"]
        result = self.git("check-ignore", "--no-index", "--", *paths)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(result.stdout.splitlines()), set(paths))

    def test_marker_is_not_ignored(self):
        result = self.git("check-ignore", "--no-index", "--",
                          "workspaces/.gitkeep")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stdout, "")

    def test_git_status_omits_local_project_and_preserves_files(self):
        self.git("rev-parse", "--show-toplevel")  # disponibilidade antes de criar
        with tempfile.TemporaryDirectory(prefix=".qa-meds-", dir=self.workspace) as temp:
            folder = Path(temp)
            asset = folder / "index.html"
            content = b"<p>Fixture descartavel de QA</p>\n"
            asset.write_bytes(content)
            relative = folder.relative_to(self.root).as_posix()
            result = self.git("status", "--porcelain", "--untracked-files=all",
                              "--", relative)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            self.assertEqual(asset.read_bytes(), content)

    def test_no_project_files_are_tracked_in_meds(self):
        result = self.git("ls-files", "--", "workspaces/")
        self.assertEqual(result.returncode, 0, result.stderr)
        tracked = set(result.stdout.splitlines()) - {"workspaces/.gitkeep"}
        self.assertFalse(tracked, f"Projetos já versionados; não removidos: {tracked}")

    def test_framework_validation_does_not_scan_projects(self):
        with tempfile.TemporaryDirectory(prefix=".qa-meds-", dir=self.workspace) as temp:
            folder = Path(temp)
            (folder / "broken.py").write_text("def (", encoding="utf-8")
            (folder / "broken.md").write_text("[link](ausente.md)\n```\n",
                                             encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                validate(self.root)


if __name__ == "__main__":
    unittest.main()
