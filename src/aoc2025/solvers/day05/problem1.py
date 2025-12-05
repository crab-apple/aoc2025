from src.aoc2025.solvers.day05.parsing import parse_ingredient_database


def solve(problem_input):
    ranges, ingredients = parse_ingredient_database(problem_input)
    count = 0
    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                count += 1
                break
    return count
