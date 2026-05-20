import unittest
from src.kmp_search import kmp_search


class TestKMPSearch(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(kmp_search("hello world", "world"), [6])

    def test_multiple_matches(self):
        self.assertEqual(kmp_search("ababcababcabc", "ababc"), [0, 5])

    def test_overlapping_matches(self):
        self.assertEqual(kmp_search("AAAA", "AA"), [0, 1, 2])

    def test_no_match(self):
        self.assertEqual(kmp_search("hello", "world"), [])

    def test_empty_needle(self):
        self.assertEqual(kmp_search("hello", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(kmp_search("", "world"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(kmp_search("hi", "hello world"), [])

    def test_full_match(self):
        self.assertEqual(kmp_search("test", "test"), [0])


if __name__ == "__main__":
    unittest.main()