import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from search_engine import STOP_WORDS, tokenize


class TokenizeTests(unittest.TestCase):
    def test_lowercases_and_splits(self):
        self.assertEqual(tokenize("Reset Password"), ["reset", "password"])

    def test_removes_stop_words(self):
        self.assertEqual(tokenize("how to reset the password"), ["reset", "password"])

    def test_strips_markdown(self):
        self.assertEqual(tokenize("# Billing **Invoice**"), ["billing", "invoice"])

    def test_strips_html_tags(self):
        self.assertEqual(tokenize("<b>refund</b> policy"), ["refund", "policy"])

    def test_drops_single_letter_tokens(self):
        self.assertEqual(tokenize("x y refund"), ["refund"])

    def test_tokens_must_start_with_a_letter(self):
        self.assertEqual(tokenize("404 error"), ["error"])
        self.assertEqual(tokenize("error404"), ["error404"])

    def test_empty_string(self):
        self.assertEqual(tokenize(""), [])

    def test_stop_words_are_lowercase(self):
        self.assertTrue(all(w == w.lower() for w in STOP_WORDS))


if __name__ == "__main__":
    unittest.main()
