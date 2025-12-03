from src.aoc2025.solvers.day03.banks import max_joltage


def solve(problem_input):
    result = 0
    for bank in problem_input.splitlines():
        result += max_joltage(int(bank), 12)
    return result
