import unittest

from src.aoc2025.solvers.day09.utils import determine_turn_direction


class TestUtils(unittest.TestCase):

    def test_turn_direction_east_L(self):
        self.assertEqual("L", determine_turn_direction([10, 10], [15, 10], [15, 5]))

    def test_turn_direction_east_R(self):
        self.assertEqual("R", determine_turn_direction([10, 10], [15, 10], [15, 15]))

    def test_turn_direction_north_L(self):
        self.assertEqual("L", determine_turn_direction([10, 10], [10, 5], [5, 5]))

    def test_turn_direction_north_R(self):
        self.assertEqual("R", determine_turn_direction([10, 10], [10, 5], [15, 5]))

    def test_turn_direction_west_L(self):
        self.assertEqual("L", determine_turn_direction([10, 10], [5, 10], [5, 15]))

    def test_turn_direction_west_R(self):
        self.assertEqual("R", determine_turn_direction([10, 10], [5, 10], [5, 5]))

    def test_turn_direction_south_L(self):
        self.assertEqual("L", determine_turn_direction([10, 10], [10, 15], [15, 15]))

    def test_turn_direction_south_R(self):
        self.assertEqual("R", determine_turn_direction([10, 10], [10, 15], [5, 15]))

    def test_turn_direction_straight(self):
        with self.assertRaises(Exception):
            determine_turn_direction([10, 10], [15, 10], [20, 10])
