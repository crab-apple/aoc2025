from src.aoc2025.solvers.day04.roll_grid import RollGrid


def solve(problem_input):
    grid = RollGrid(problem_input)
    return grid.count_accessible()
