from src.aoc2025.solvers.day02.ids import find_invalid_ids
from src.aoc2025.solvers.day02.input_parsing import parse_input


def solve(problem_input):
    ranges = parse_input(problem_input)

    result = 0
    for rge in ranges:
        for invalid_id in find_invalid_ids(rge):
            result += invalid_id

    return result
