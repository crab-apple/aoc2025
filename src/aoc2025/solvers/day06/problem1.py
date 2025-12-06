from src.aoc2025.solvers.day06.parsing import parse_input


def solve(problem_input):
    result = 0
    for operation in parse_input(problem_input):
        result += operation.execute()

    return result
