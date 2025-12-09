import os
import textwrap
import unittest

from src.aoc2025.solvers.day09.problem2 import solve


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
        self.assertEqual(24, solve(example_input))

    def test_real_input(self):
        dirname = os.path.dirname(__file__)
        input_file_path = os.path.join(dirname, "../../inputs/day09/input")
        with open(input_file_path, "r") as file:
            problem_input = file.read()
        self.assertIsNotNone(solve(problem_input))
