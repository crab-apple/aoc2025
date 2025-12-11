import os
import textwrap
import unittest

from src.aoc2025.solvers.day10.problem2 import solve


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
            [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
            [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
            """
        ).strip()
        self.assertEqual(33, solve(example_input))

    def test_performance(self):
        dirname = os.path.dirname(__file__)
        input_file_path = os.path.join(dirname, "../../inputs/day10/input")
        with open(input_file_path, "r") as file:
            problem_input = file.read()

        problem_input = _first_n_lines(problem_input, 1)
        print(problem_input)

        self.assertIsNotNone(solve(problem_input))


def _first_n_lines(problem_input, n):
    return "\n".join(problem_input.splitlines()[0:n])
