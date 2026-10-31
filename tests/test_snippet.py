import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from search_engine import extract_snippet


class SnippetTests(unittest.TestCase):
    def test_short_text_is_returned_with_ellipsis(self):
        snippet = extract_snippet("Refunds depend on policy.", ["refund"])
        self.assertIn("Refunds", snippet)
        self.assertTrue(snippet.endswith("..."))

    def test_snippet_centres_on_late_match(self):
        text = ("filler " * 100) + "the refund policy is here. " + ("more " * 100)
        snippet = extract_snippet(text, ["refund"], window=120)
        self.assertIn("refund", snippet)
        self.assertTrue(snippet.startswith("..."))

    def test_snippet_is_not_much_longer_than_window(self):
        text = "word " * 500
        snippet = extract_snippet(text, ["word"], window=100)
        self.assertLessEqual(len(snippet), 100 + 10)

    def test_no_match_returns_start_of_text(self):
        snippet = extract_snippet("Billing questions include invoices.", ["zzz"])
        self.assertTrue(snippet.startswith("Billing"))


if __name__ == "__main__":
    unittest.main()
