import unittest

from beer_party import solve_beers

class TestBeerParty(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(solve_beers(2, 2, "YN NY"), 2)

    def test_example_2(self):
        self.assertEqual(solve_beers(6, 3, "YNN YNY YNY NYY NYY NYN"), 2)

    def test_all_like_one_beer(self):
        self.assertEqual(solve_beers(3, 2, "NY NY NY"), 1)

    def test_all_like_all_beers(self):
        self.assertEqual(solve_beers(3, 3, "YYY YYY YYY"), 1)

    def test_everyone_needs_unique_beer(self):
        self.assertEqual(solve_beers(4, 4, "YNNN NYNN NNYN NNNY"), 4)

    def test_single_employee(self):
        self.assertEqual(solve_beers(1, 1, "Y"), 1)

    def test_complex_coverage(self):
        self.assertEqual(solve_beers(5, 5, "YYNNN NYYNN NNYYN NNNYY YNNNY"), 3)

if __name__ == '__main__':
    unittest.main()