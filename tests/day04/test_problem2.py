from aoc2025.solvers.day04.problem2 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
        EXAMPLE
        INPUT
        """
        ).strip()
        self.assertEqual("TODO EXPECTED OUTPUT", solve(example_input))
