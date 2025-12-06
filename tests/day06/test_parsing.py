import unittest

from src.aoc2025.solvers.day06.parsing import find_whitespace


class TestParsing(unittest.TestCase):

    def test_find_whitespace(self):
        # Given
        the_input = " 45 64  387 23 "

        # When
        space_positions = find_whitespace(the_input)

        # Then
        self.assertEqual({0, 3, 6, 7, 11, 14}, space_positions)
