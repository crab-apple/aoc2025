import textwrap
import unittest

from src.aoc2025.solvers.day09.problem1 import solve


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            7,1
            11,1
            11,7
            9,7
            9,5
            2,5
            2,3
            7,3
        """
        ).strip()
        self.assertEqual(50, solve(example_input))
