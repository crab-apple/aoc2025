from src.aoc2025.solvers.day06.problem2 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            123 328  51 64 
             45 64  387 23 
              6 98  215 314
            *   +   *   +  
        """
        ).strip()
        self.assertEqual(3263827, solve(example_input))
