from src.aoc2025.solvers.day04.problem1 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
        """
        ).strip()
        self.assertEqual(13, solve(example_input))
