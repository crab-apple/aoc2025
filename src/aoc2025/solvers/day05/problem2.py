from src.aoc2025.solvers.day05.parsing import parse_ingredient_database
from src.aoc2025.solvers.day05.range_merge import merge_ranges


def solve(problem_input):
    ranges, ingredients = parse_ingredient_database(problem_input)
    merged_ranges = merge_ranges(ranges)
    count = 0
    for r in merged_ranges:
        count += r[1] - r[0] + 1
    return count
