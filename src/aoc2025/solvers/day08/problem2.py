from src.aoc2025.disjoint_set_forest.disjoint_set_forest import DisjointSetForest
from src.aoc2025.solvers.day08.distances import calculate_distances
from src.aoc2025.solvers.day08.input_parsing import parse_input


def solve(
    problem_input,
):
    boxes = parse_input(problem_input)

    # Compute distances
    distances = calculate_distances(boxes)
    sorted_distances = list(sorted(distances, key=lambda d: d.value, reverse=True))

    # Prepare forest
    forest = DisjointSetForest(len(boxes))

    # Connect boxes
    num_separate_circuits = len(boxes)
    while True:
        next_connection = sorted_distances.pop()
        boxes_to_connect = list(next_connection.boxes)
        box_a = boxes_to_connect[0]
        box_b = boxes_to_connect[1]
        if forest.find(box_a) == forest.find(box_b):
            # Boxes already in the same circuit, no need to connect
            continue
        # Connect the boxes, bringing two circuits into one
        forest.merge(box_a, box_b)
        num_separate_circuits -= 1
        if num_separate_circuits == 1:
            # Done!
            return boxes[box_a].coords[0] * boxes[box_b].coords[0]
