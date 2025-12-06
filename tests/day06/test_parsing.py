import textwrap
import unittest

from src.aoc2025.solvers.day06.operation import Operation
from src.aoc2025.solvers.day06.parsing import (
    find_whitespace,
    find_breakpoints,
    parse_input,
)


class TestParsing(unittest.TestCase):

    def test_find_whitespace(self):
        # Given
        the_input = " 45 64  387 23 "

        # When
        space_positions = find_whitespace(the_input)

        # Then
        self.assertEqual({0, 3, 6, 7, 11, 14}, space_positions)

    def test_find_breakpoints(self):
        # Given
        the_input = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]

        # When
        breakpoints = find_breakpoints(the_input)

        # Then
        self.assertEqual([3, 7, 11], breakpoints)

    def test_parse_input(self):
        # Given
        the_input = textwrap.dedent(
            """\
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  
        """
        )

        # When
        operations = parse_input(the_input)

        # Then
        expected = [
            Operation(["123", " 45", "  6"], "*"),
            Operation(["328", "64 ", "98 "], "+"),
            Operation([" 51", "387", "215"], "*"),
            Operation(["64 ", "23 ", "314"], "+"),
        ]
        self.assertEqual(expected, operations)
