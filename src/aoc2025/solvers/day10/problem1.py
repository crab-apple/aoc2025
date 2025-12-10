from src.aoc2025.solvers.day10.input_parsing import parse_input
from src.aoc2025.solvers.day10.path_finding import shortest_path


def solve(problem_input):
    machines = parse_input(problem_input)
    result = 0
    for machine in machines:
        result += shortest_path(machine.goal, machine.buttons)
    return result
