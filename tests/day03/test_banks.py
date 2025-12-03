from src.aoc2025.solvers.day03.banks import max_joltage

import unittest


class TestBanks(unittest.TestCase):

    def test_two_digits(self):
        self.assertEqual(11, max_joltage(11))

    def test_several_digits_max_joltage_consecutive_at_start(self):
        self.assertEqual(55, max_joltage(55111))

    def test_several_digits_max_joltage_consecutive_middle(self):
        self.assertEqual(55, max_joltage(11155111))

    def test_several_digits_not_consecutive(self):
        self.assertEqual(42, max_joltage(11141122111))

    def test_several_digits_not_consecutive_inverted(self):
        self.assertEqual(41, max_joltage(11121124111))

    def test_several_digits_max_at_end(self):
        self.assertEqual(89, max_joltage(111811119))

    def test_more_than_two_picks(self):
        self.assertEqual(434234234278, max_joltage(234234234234278, 12))
