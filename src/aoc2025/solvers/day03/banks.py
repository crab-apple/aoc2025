def max_joltage(bank, digits=2):
    return int(_max_joltage_str(str(bank), 0, digits))


def _max_joltage_str(bank, start, digits):
    if digits == 0:
        return ""
    first_pos = _max_position(bank, start, digits - 1)
    return bank[first_pos] + _max_joltage_str(bank, first_pos + 1, digits - 1)


def _max_position(bank, starting_index, remaining_digits):
    if remaining_digits == 0:
        candidates = bank[starting_index:]
    else:
        candidates = bank[starting_index:-remaining_digits]
    return bank.index(max(candidates), starting_index)
