from aoc2025.solvers.day01.dial import Dial
import unittest


class TestDial(unittest.TestCase):

    def test_starts_at_0(self):
        # Given
        dial = Dial()

        # Then
        self.assertEqual(0, dial.pointer())

    def test_rotates_right(self):
        # Given
        dial = Dial()

        # When
        dial.rotate("R", 12)

        # Then
        self.assertEqual(12, dial.pointer())

    def test_rotates_multiple_times(self):
        # Given
        dial = Dial()
        dial.rotate("R", 1)

        # When
        dial.rotate("R", 2)

        # Then
        self.assertEqual(3, dial.pointer())

    def test_rotates_left(self):
        # Given
        dial = Dial()
        dial.rotate("R", 10)

        # When
        dial.rotate("L", 3)

        # Then
        self.assertEqual(7, dial.pointer())

    def test_rotating_right_wraps(self):
        # Given
        dial = Dial()

        # When
        dial.rotate("R", 50)
        dial.rotate("R", 50)

        # Then
        self.assertEqual(0, dial.pointer())

    def test_rotating_left_wraps_to_0(self):
        # Given
        dial = Dial()

        # When
        dial.rotate("L", 50)
        dial.rotate("L", 50)

        # Then
        self.assertEqual(0, dial.pointer())

    def test_rotating_left_wraps_to_positive(self):
        # Given
        dial = Dial()

        # When
        dial.rotate("L", 1)

        # Then
        self.assertEqual(99, dial.pointer())

    def test_rejects_invalid_rotation_direction(self):
        # Given
        dial = Dial()

        # Then
        self.assertRaises(ValueError, dial.rotate, "A", 12)

    def test_rejects_invalid_rotation_type(self):
        # Given
        dial = Dial()

        # Then
        self.assertRaises(TypeError, dial.rotate, 1, 12)

    def test_rotate_right_clicks_no_times(self):
        # Given
        dial = Dial()

        # When
        clicks = dial.rotate("R", 10)

        # Then
        self.assertEqual(0, clicks)

    def test_rotate_right_clicks_one_time(self):
        # Given
        dial = Dial()

        # When
        clicks = dial.rotate("R", 110)

        # Then
        self.assertEqual(1, clicks)

    def test_rotate_right_clicks_many_times(self):
        # Given
        dial = Dial()
        clicks = dial.rotate("R", 10)

        # When
        clicks = dial.rotate("R", 123000)

        # Then
        self.assertEqual(1230, clicks)

    def test_rotate_left_from_zero_clicks_no_times(self):
        # Given
        dial = Dial()

        # When
        clicks = dial.rotate("L", 5)

        # Then
        self.assertEqual(0, clicks)

    def test_rotate_left_from_zero_clicks_many_times(self):
        # Given
        dial = Dial()

        # When
        clicks = dial.rotate("L", 250)

        # Then
        self.assertEqual(2, clicks)
