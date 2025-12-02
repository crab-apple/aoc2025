import unittest

from src.aoc2025.solvers.day02.ids import (
    next_invalid_id,
    prev_invalid_id,
    extract_first_half,
    extract_second_half,
)


class TestNextInvalidId(unittest.TestCase):

    def test_even_digits_equal_halves(self):
        self.assertEqual(1212, next_invalid_id(1212))

    def test_even_digits_first_half_greater(self):
        self.assertEqual(654654, next_invalid_id(654321))

    def test_even_digits_first_half_lower(self):
        self.assertEqual(124124, next_invalid_id(123456))

    def test_uneven_digits(self):
        self.assertEqual(100100, next_invalid_id(12345))

    def test_zero(self):
        self.assertEqual(11, next_invalid_id(0))

    def test_single_digit(self):
        self.assertEqual(11, next_invalid_id(3))


class TestPrevInvalidId(unittest.TestCase):

    def test_even_digits_equal_halves(self):
        self.assertEqual(1212, prev_invalid_id(1212))

    def test_even_digits_first_half_greater(self):
        self.assertEqual(653653, prev_invalid_id(654321))

    def test_even_digits_first_half_lower(self):
        self.assertEqual(123123, prev_invalid_id(123456))

    def test_uneven_digits(self):
        self.assertEqual(9999, prev_invalid_id(12345))

    def test_zero(self):
        self.assertIsNone(prev_invalid_id(0))

    def test_single_digit(self):
        self.assertIsNone(prev_invalid_id(3))


class TestManipulators(unittest.TestCase):
    def test_first_half(self):
        self.assertEqual(12, extract_first_half(1234))
        self.assertEqual(123, extract_first_half(123456))

    def test_second_half(self):
        self.assertEqual(34, extract_second_half(1234))
        self.assertEqual(456, extract_second_half(123456))
