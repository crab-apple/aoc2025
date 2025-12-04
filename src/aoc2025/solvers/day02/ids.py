import math

from src.aoc2025.solvers.day02.invalid_id import InvalidId


def find_invalid_ids(rge):
    first = next_invalid_id(rge[0]).as_int()
    last = prev_invalid_id(rge[1])
    result = []
    if last is None:
        return []
    while first <= last.as_int():
        result.append(first)
        first = next_invalid_id(first + 1).as_int()

    return result


def next_invalid_id(number):
    """Returns the lowest invalid ID that is equal or greater to the given number."""

    number1 = _num_digits(number)
    if not number1 % 2 == 0:
        return InvalidId((math.floor(math.pow(10, _num_digits(number) // 2))), 2)

    first_part = _extract_first_part(number)
    invalid_id_from_first_part = InvalidId(first_part, 2)
    if invalid_id_from_first_part.as_int() < number:
        return InvalidId(first_part + 1, 2)
    return InvalidId(first_part, 2)


def prev_invalid_id(number):
    """Returns the largest invalid ID that is equal or lower than the given number.

    Returns None if there is no invalid ID that satisfies these conditions"""

    invalid_id = next_invalid_id(number)

    if invalid_id.as_int() == number:
        return invalid_id

    return invalid_id.prev()


def _extract_first_part(number, num_parts=2):
    num_digits = _num_digits(number)
    return int(str(number)[0 : (num_digits // num_parts)])


def _num_digits(number):
    return len(str(number))
