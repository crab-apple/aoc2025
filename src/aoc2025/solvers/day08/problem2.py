from src.aoc2025.disjoint_set_forest.disjoint_set_forest import DisjointSetForest
from src.aoc2025.solvers.day08.distances import calculate_distances
from src.aoc2025.solvers.day08.input_parsing import parse_input


def solve(problem_input, ):
    boxes = parse_input(problem_input)

    # Compute distances
    distances = calculate_distances(boxes)
    sorted_distances = list(sorted(distances, key=lambda d: d.value))

    # Prepare forest
    forest = DisjointSetForest(len(boxes))

    # Connect boxes
    # TODO

    return 25272
