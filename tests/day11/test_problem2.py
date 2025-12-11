import os
import textwrap
import unittest

from src.aoc2025.solvers.day11.problem2 import solve


class TestProblem(unittest.TestCase):

    def test_example_input(self):
        example_input = textwrap.dedent(
            """
            svr: aaa bbb
            aaa: fft
            fft: ccc
            bbb: tty
            tty: ccc
            ccc: ddd eee
            ddd: hub
            hub: fff
            eee: dac
            dac: fff
            fff: ggg hhh
            ggg: out
            hhh: out 
        """
        ).strip()
        self.assertEqual(2, solve(example_input))

    def test_real_input(self):
        dirname = os.path.dirname(__file__)
        input_file_path = os.path.join(dirname, "../../inputs/day11/input")
        with open(input_file_path, "r") as file:
            problem_input = file.read()
        self.assertEqual(520476725037672, solve(problem_input))
