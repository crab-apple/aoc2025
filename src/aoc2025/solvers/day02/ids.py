import math

from src.aoc2025.solvers.day02.invalid_id import InvalidId


def find_invalid_ids(rge):
    result = set()
    for num_parts in range(2, len(str(rge))):
        result = result.union(set(find_invalid_ids_given_num_parts(rge, num_parts)))

    return result


def find_invalid_ids_given_num_parts(rge, num_parts=2):
    first = next_invalid_id(rge[0], num_parts)
    last = prev_invalid_id(rge[1], num_parts)
    result = []
    if last is None:
        return []
    while first.as_int() <= last.as_int():
        result.append(first.as_int())
        first = first.next()

    return result


def next_invalid_id(number, num_parts=2):
    """Returns the lowest invalid ID that is equal or greater to the given number."""

    if _num_digits(number) < num_parts:
        return InvalidId(1, num_parts)

    if not _num_digits(number) % num_parts == 0:
        return InvalidId(
            (math.floor(math.pow(10, _num_digits(number) // num_parts))), num_parts
        )

    first_part = _extract_first_part(number, num_parts)
    invalid_id_from_first_part = InvalidId(first_part, num_parts)
    if invalid_id_from_first_part.as_int() < number:
        return InvalidId(first_part + 1, num_parts)
    return InvalidId(first_part, num_parts)


def prev_invalid_id(number, num_parts=2):
    """Returns the largest invalid ID that is equal or lower than the given number.

    Returns None if there is no invalid ID that satisfies these conditions"""

    invalid_id = next_invalid_id(number, num_parts)

    if invalid_id.as_int() == number:
        return invalid_id

    return invalid_id.prev()


def _extract_first_part(number, num_parts=2):
    num_digits = _num_digits(number)
    return int(str(number)[0 : (num_digits // num_parts)])


def _num_digits(number):
    return len(str(number))
