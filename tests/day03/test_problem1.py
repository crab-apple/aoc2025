from aoc2025.solvers.day03.problem1 import solve
import textwrap
import unittest


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            987654321111111
            811111111111119
            234234234234278
            818181911112111
        """
        ).strip()
        self.assertEqual(357, solve(example_input))
