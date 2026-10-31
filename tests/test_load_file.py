import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import contextlib
import io
import json
import tempfile

import search_engine
from search_engine import load_file


class LoadFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_markdown_is_returned_as_text(self):
        path = self.root / "a.md"
        path.write_text("# Title\nBody")
        self.assertEqual(load_file(path), "# Title\nBody")

    def test_json_is_pretty_printed(self):
        path = self.root / "a.json"
        path.write_text('{"a": 1}')
        self.assertEqual(load_file(path), json.dumps({"a": 1}, indent=2))

    def test_invalid_json_falls_back_to_raw_text(self):
        path = self.root / "bad.json"
        path.write_text("{bad")
        self.assertEqual(load_file(path), "{bad")

    def test_missing_file_returns_none(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(load_file(self.root / "missing.md"))

    @unittest.skipIf(search_engine.HAS_PDF, "PyPDF2 is installed")
    def test_pdf_without_library_returns_none(self):
        path = self.root / "a.pdf"
        path.write_bytes(b"%PDF-1.4")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(load_file(path))


if __name__ == "__main__":
    unittest.main()
