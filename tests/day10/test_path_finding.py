import unittest

from src.aoc2025.solvers.day10.path_finding import shortest_path


class TestPathFinding(unittest.TestCase):

    def test_finds_path_of_length_0(self):
        length = shortest_path(set(), [{1, 2, 3}])

        self.assertEqual(0, length)

    def test_finds_path_of_length_1(self):
        length = shortest_path({2}, [{1, 2, 3}, {2}])

        self.assertEqual(1, length)
