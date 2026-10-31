import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from search_engine import normalize_tokens, stem


class StemTests(unittest.TestCase):
    def test_plural_s_is_removed(self):
        self.assertEqual(stem("passwords"), "password")
        self.assertEqual(stem("refunds"), "refund")

    def test_ies_becomes_y(self):
        self.assertEqual(stem("policies"), "policy")

    def test_ing_is_removed(self):
        self.assertEqual(stem("billing"), "bill")

    def test_double_s_is_kept(self):
        self.assertEqual(stem("access"), "access")

    def test_short_words_are_unchanged(self):
        self.assertEqual(stem("is"), "is")
        self.assertEqual(stem("api"), "api")

    def test_normalize_tokens_stems_each_token(self):
        self.assertEqual(normalize_tokens(["refunds", "billing"]), ["refund", "bill"])

    def test_normalize_tokens_empty(self):
        self.assertEqual(normalize_tokens([]), [])


if __name__ == "__main__":
    unittest.main()
