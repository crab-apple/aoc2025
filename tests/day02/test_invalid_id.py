import unittest

from src.aoc2025.solvers.day02.invalid_id import InvalidId


class TestInvalidId(unittest.TestCase):

    def test_to_int(self):
        # Given
        invalid_id = InvalidId(123, 3)

        # Then
        self.assertEqual(123123123, invalid_id.as_int())

    def test_next(self):
        # Given
        invalid_id = InvalidId(123, 3)

        # Then
        self.assertEqual(124124124, invalid_id.next().as_int())

    def test_prev(self):
        # Given
        invalid_id = InvalidId(100, 3)

        # Then
        self.assertEqual(999999, invalid_id.prev().as_int())

    def test_prev_from_1(self):
        # Given
        invalid_id = InvalidId(1, 3)

        # Then
        self.assertIsNone(invalid_id.prev())
