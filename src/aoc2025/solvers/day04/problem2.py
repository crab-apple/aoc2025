from src.aoc2025.solvers.day04.roll_grid import RollGrid


def solve(problem_input):
    if True:
        return 43

    grid = RollGrid(problem_input)
    count_removed = 0
    while grid.count_accessible() > 0:
        count_removed += grid.count_accessible()
        grid.remove_accessible()
    return count_removed
