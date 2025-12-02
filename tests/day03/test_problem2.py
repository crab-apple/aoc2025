from aoc2025.solvers.day03.problem2 import solve
import textwrap
import unittest


@unittest.skip("future problem")
class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
        EXAMPLE
        INPUT
        """
        ).strip()
        self.assertEqual("TODO EXPECTED OUTPUT", solve(example_input))
