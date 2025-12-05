import unittest

from src.aoc2025.solvers.day05.range_merge import merge_ranges


class TestRangeMerge(unittest.TestCase):

    def test_separate_ranges(self):
        self.assertEqual(
            [(1, 2), (3, 4)],
            merge_ranges([(1, 2), (3, 4)])
        )

    def test_overlapping_ranges(self):
        self.assertEqual(
            [(1, 10), (20, 30)],
            merge_ranges([(1, 10), (20, 25), (22, 30)])
        )

    def test_subsuming_ranges(self):
        self.assertEqual(
            [(1, 10), (20, 30)],
            merge_ranges([(1, 10), (20, 30), (22, 25)])
        )

    def test_unordered_ranges(self):
        self.assertEqual(
            [(1, 10), (20, 30)],
            merge_ranges([(20, 30), (1, 10), (22, 25)])
        )
