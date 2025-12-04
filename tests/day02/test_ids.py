import unittest

from src.aoc2025.solvers.day02.ids import (
    next_invalid_id,
    prev_invalid_id,
    find_invalid_ids_given_num_parts,
)


class TestNextInvalidId(unittest.TestCase):

    def test_even_digits_equal_halves(self):
        self.assertEqual(1212, next_invalid_id(1212).as_int())

    def test_even_digits_first_half_greater(self):
        self.assertEqual(654654, next_invalid_id(654321).as_int())

    def test_even_digits_first_half_lower(self):
        self.assertEqual(124124, next_invalid_id(123456).as_int())

    def test_uneven_digits(self):
        self.assertEqual(100100, next_invalid_id(12345).as_int())

    def test_zero(self):
        self.assertEqual(11, next_invalid_id(0).as_int())

    def test_single_digit(self):
        self.assertEqual(11, next_invalid_id(3).as_int())

    def test_more_than_two_parts(self):
        self.assertEqual(656565, next_invalid_id(654321, 3).as_int())


class TestPrevInvalidId(unittest.TestCase):

    def test_even_digits_equal_halves(self):
        self.assertEqual(1212, prev_invalid_id(1212).as_int())

    def test_even_digits_first_half_greater(self):
        self.assertEqual(653653, prev_invalid_id(654321).as_int())

    def test_even_digits_first_half_lower(self):
        self.assertEqual(123123, prev_invalid_id(123456).as_int())

    def test_uneven_digits(self):
        self.assertEqual(9999, prev_invalid_id(12345).as_int())

    def test_zero(self):
        self.assertIsNone(prev_invalid_id(0))

    def test_single_digit(self):
        self.assertIsNone(prev_invalid_id(3))

    def test_more_than_two_parts(self):
        self.assertEqual(646464, prev_invalid_id(654321, 3).as_int())

    def test_failing_example(self):
        self.assertEqual(111, prev_invalid_id(115, 3).as_int())


class TestFindInvalidIds(unittest.TestCase):
    def test_exercise_examples(self):
        self.assertEqual([11, 22], find_invalid_ids_given_num_parts((11, 22)))
        self.assertEqual([99], find_invalid_ids_given_num_parts((95, 115)))
        self.assertEqual([1010], find_invalid_ids_given_num_parts((998, 1012)))
        self.assertEqual(
            [1188511885], find_invalid_ids_given_num_parts((1188511880, 1188511890))
        )
        self.assertEqual([222222], find_invalid_ids_given_num_parts((222220, 222224)))
        self.assertEqual([], find_invalid_ids_given_num_parts((1698522, 1698528)))
        self.assertEqual([446446], find_invalid_ids_given_num_parts((446443, 446449)))
        self.assertEqual(
            [38593859], find_invalid_ids_given_num_parts((38593856, 38593862))
        )

    def test_inverted_range(self):
        self.assertEqual([], find_invalid_ids_given_num_parts((123000, 100)))

    def test_low_second_number(self):
        self.assertEqual([], find_invalid_ids_given_num_parts((1, 2)))

    def test_exercise_examples_different_num_parts(self):
        self.assertEqual([11, 22], find_invalid_ids_given_num_parts((11, 22), 2))
        self.assertEqual([99], find_invalid_ids_given_num_parts((95, 115), 2))
        self.assertEqual([111], find_invalid_ids_given_num_parts((95, 115), 3))
        self.assertEqual(
            [], find_invalid_ids_given_num_parts((2121212118, 2121212124), 2)
        )
        self.assertEqual(
            [], find_invalid_ids_given_num_parts((2121212118, 2121212124), 3)
        )
        self.assertEqual(
            [], find_invalid_ids_given_num_parts((2121212118, 2121212124), 4)
        )
        self.assertEqual(
            [2121212121], find_invalid_ids_given_num_parts((2121212118, 2121212124), 5)
        )
