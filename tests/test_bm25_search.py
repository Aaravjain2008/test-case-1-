import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import contextlib
import io
import tempfile

from search_engine import BM25Index


class BM25SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        (root / "refunds.md").write_text(
            "Refund eligibility depends on the refund policy. Do not promise a refund."
        )
        (root / "billing.md").write_text(
            "Billing questions include invoices and payment failures."
        )
        (root / "passwords.md").write_text(
            "Forgotten password? Use the official password reset process."
        )
        cls.index = BM25Index()
        with contextlib.redirect_stdout(io.StringIO()):
            cls.index.build(root)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_index_contains_all_documents(self):
        self.assertEqual(self.index.N, 3)

    def test_refund_query_ranks_refunds_first(self):
        results = self.index.search("refund policy")
        self.assertEqual(results[0]["filename"], "refunds.md")

    def test_password_query_ranks_passwords_first(self):
        results = self.index.search("password reset")
        self.assertEqual(results[0]["filename"], "passwords.md")

    def test_ranks_are_sequential_and_scores_descending(self):
        results = self.index.search("refund payment password")
        self.assertEqual([r["rank"] for r in results], list(range(1, len(results) + 1)))
        scores = [r["score"] for r in results]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_top_n_limits_results(self):
        self.assertEqual(len(self.index.search("refund payment password", top_n=1)), 1)

    def test_empty_query_returns_nothing(self):
        self.assertEqual(self.index.search(""), [])

    def test_stop_word_only_query_returns_nothing(self):
        self.assertEqual(self.index.search("the and of"), [])

    def test_unknown_term_returns_nothing(self):
        self.assertEqual(self.index.search("zzzzqqq"), [])

    def test_empty_index_returns_nothing(self):
        self.assertEqual(BM25Index().search("refund"), [])


if __name__ == "__main__":
    unittest.main()
