import unittest
import os
import csv
from src.lab7_2_2 import (
    calculate_minimum_cable_length,
)


class TestNetworkSolver(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_wells.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_csv(self, data):
        with open(self.test_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def test_standard_case(self):
        data = [
            ["K1", "K2", "2000"],
            ["K2", "K3", "1500"],
            ["K1", "K3", "3000"],
            ["K3", "K4", "500"],
        ]
        self.create_csv(data)
        self.assertEqual(calculate_minimum_cable_length(self.test_file), 4000)

    def test_disconnected_graph(self):
        data = [
            ["K1", "K2", "1000"],
            ["K3", "K4", "2000"],
        ]
        self.create_csv(data)
        self.assertEqual(calculate_minimum_cable_length(self.test_file), -1)

    def test_empty_file(self):
        self.create_csv([])
        self.assertEqual(calculate_minimum_cable_length(self.test_file), 0)

    def test_single_edge(self):
        data = [["K1", "K2", "500"]]
        self.create_csv(data)
        self.assertEqual(calculate_minimum_cable_length(self.test_file), 500)


if __name__ == "__main__":
    unittest.main()
