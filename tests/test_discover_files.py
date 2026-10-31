import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import tempfile

from search_engine import discover_files


class DiscoverFilesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "a.md").write_text("alpha")
        (self.root / "b.txt").write_text("beta")
        (self.root / "c.exe").write_text("binary")
        (self.root / "sub").mkdir()
        (self.root / "sub" / "e.md").write_text("epsilon")
        (self.root / ".hidden").mkdir()
        (self.root / ".hidden" / "d.md").write_text("delta")

    def tearDown(self):
        self.tmp.cleanup()

    def names(self, files):
        return sorted(p.name for p in files)

    def test_recursive_finds_supported_files_only(self):
        self.assertEqual(self.names(discover_files(self.root)), ["a.md", "b.txt", "e.md"])

    def test_non_recursive_skips_subfolders(self):
        files = discover_files(self.root, recursive=False)
        self.assertEqual(self.names(files), ["a.md", "b.txt"])

    def test_hidden_folders_are_skipped(self):
        self.assertNotIn("d.md", self.names(discover_files(self.root)))

    def test_missing_folder_raises(self):
        with self.assertRaises(FileNotFoundError):
            discover_files(self.root / "does-not-exist")


if __name__ == "__main__":
    unittest.main()
