from src.aoc2025.solvers.day02.ids import find_invalid_ids


def solve(problem_input):
    ranges = _parse_input(problem_input)

    result = 0
    for rge in ranges:
        for invalid_id in find_invalid_ids(rge):
            result += invalid_id

    return result


def _parse_input(problem_input):
    result = []
    for part in problem_input.split(","):
        rge = int(part.split("-")[0]), int(part.split("-")[1])
        result.append(rge)

    return result
