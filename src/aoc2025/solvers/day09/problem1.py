from src.aoc2025.solvers.day09.utils import area_between, parse_tiles


def solve(problem_input):
    tiles = parse_tiles(problem_input)

    max_area = 0
    for i in range(0, len(tiles)):
        for j in range(i + 1, len(tiles)):
            max_area = max(max_area, area_between(tiles[i], tiles[j]))

    return max_area
