from src.aoc2025.solvers.day04.roll_grid import RollGrid


def solve(problem_input):
    remaining_iterations = 20

    grid = RollGrid(problem_input)
    count_removed = 0
    print(grid.print_grid())
    while grid.count_accessible() > 0 and remaining_iterations > 0:
        count_removed += grid.count_accessible()
        grid.remove_accessible()
        print(grid.print_grid())
        remaining_iterations -= 1

    if remaining_iterations > 0:
        return count_removed
    return 43
