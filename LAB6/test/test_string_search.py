import unittest
from src.string_search import kmp_search


class TestKMPSearch(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(kmp_search("hello world", "world"), [6])

    def test_multiple_occurrences(self):
        self.assertEqual(kmp_search("ababcababcabc", "ababc"), [0, 5])

    def test_overlapping_occurrences(self):
        self.assertEqual(kmp_search("AAAA", "AA"), [0, 1, 2])

    def test_no_occurrence(self):
        self.assertEqual(kmp_search("hello world", "python"), [])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("hello", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(kmp_search("", "hello"), [])

    def test_both_empty(self):
        self.assertEqual(kmp_search("", ""), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(kmp_search("short", "muchlongerneedle"), [])

    def test_full_match(self):
        self.assertEqual(kmp_search("exactmatch", "exactmatch"), [0])


if __name__ == "__main__":
    unittest.main()
