import unittest

from src.aoc2025.solvers.day06.operation import Operation


class TestOperation(unittest.TestCase):

    def test_addition(self):
        op = Operation([" 1 ", " 2 ", " 4 "], "+")
        self.assertEqual(7, op.execute())

    def test_multiplication(self):
        op = Operation([" 1 ", " 2 ", " 4 "], "*")
        self.assertEqual(8, op.execute())

    def test_uncephalopodize(self):
        op = Operation(["64 ", "23 ", "314"], "+")
        expected = Operation(["623", "431", "  4"], "+")
        self.assertEqual(expected, op.uncephalopodize())
        self.assertEqual(op, op.uncephalopodize().uncephalopodize())
