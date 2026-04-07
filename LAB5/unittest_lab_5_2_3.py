import unittest
from lab_5_2_3 import min_knight_moves

class TestKnightMoves(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(min_knight_moves(8, (7, 0), (0, 7)), 6)

    def test_same_start_and_end(self):
        self.assertEqual(min_knight_moves(8, (3, 3), (3, 3)), 0)

    def test_one_move(self):
        self.assertEqual(min_knight_moves(8, (0, 0), (2, 1)), 1)
        self.assertEqual(min_knight_moves(8, (4, 4), (5, 6)), 1)

    def test_two_moves(self):
        self.assertEqual(min_knight_moves(8, (0, 0), (0, 2)), 2)

    def test_unreachable_target(self):
        self.assertEqual(min_knight_moves(3, (0, 0), (1, 1)), -1)

    def test_large_board(self):
        self.assertEqual(min_knight_moves(20, (0, 0), (19, 19)), 14)

if __name__ == '__main__':
    unittest.main()