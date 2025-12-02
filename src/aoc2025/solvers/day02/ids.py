import math


def find_invalid_ids(rge):
    first = next_invalid_id(rge[0])
    last = prev_invalid_id(rge[1])
    result = []
    if last is None:
        return []
    while first <= last:
        result.append(first)
        first = next_invalid_id(first + 1)

    return result


def next_invalid_id(number):
    """Returns the lowest invalid ID that is equal or greater to the given number."""

    if not _is_even(_num_digits(number)):
        return _repeat(math.floor(math.pow(10, _num_digits(number) // 2)))

    first_half = extract_first_half(number)
    second_half = extract_second_half(number)
    if first_half < second_half:
        return _repeat(first_half + 1)
    return _repeat(first_half)


def prev_invalid_id(number):
    """Returns the largest invalid ID that is equal or lower than the given number.

    Returns None if there is no invalid ID that satisfies these conditions"""
    if _is_invalid_id(number):
        return number

    half = extract_first_half(next_invalid_id(number))
    if half == 1:
        return None
    return _repeat(half - 1)


def extract_first_half(number):
    num_digits = _num_digits(number)
    return int(str(number)[0 : (num_digits // 2)])


def extract_second_half(number):
    num_digits = _num_digits(number)
    return int(str(number)[(num_digits // 2) : num_digits])


def _repeat(number):
    return int(str(number) + str(number))


def _is_invalid_id(number):
    return len(str(number)) % 2 == 0 and extract_first_half(
        number
    ) == extract_second_half(number)


def _num_digits(number):
    return len(str(number))


def _is_even(number):
    return number % 2 == 0
