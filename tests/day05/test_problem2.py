from src.aoc2025.solvers.day05.problem2 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            3-5
            10-14
            16-20
            12-18
            
            1
            5
            8
            11
            17
            32
        """
        ).strip()
        self.assertEqual(14, solve(example_input))
