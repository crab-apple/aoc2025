from aoc2025.solvers.day01.problem2 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            L68
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82
        """
        ).strip()
        self.assertEqual(6, solve(example_input))
