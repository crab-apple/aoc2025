from src.aoc2025.solvers.day08.junction_box import JunctionBox


def parse_input(problem_input):
    result = []
    id_counter = 0
    for line in problem_input.splitlines():
        coords = list(map(int, line.split(",")))
        result.append(JunctionBox(id_counter, coords))
        id_counter += 1

    return result
