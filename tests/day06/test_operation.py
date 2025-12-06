import unittest

from src.aoc2025.solvers.day06.operation import Operation


class TestOperation(unittest.TestCase):

    def test_addition(self):
        op = Operation([" 1 ", " 2 ", " 4 "], "+")
        self.assertEqual(7, op.execute())

    def test_multiplication(self):
        op = Operation([" 1 ", " 2 ", " 4 "], "*")
        self.assertEqual(8, op.execute())
