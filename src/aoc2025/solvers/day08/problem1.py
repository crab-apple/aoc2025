from src.aoc2025.disjoint_set_forest.disjoint_set_forest import DisjointSetForest
from src.aoc2025.solvers.day08.distances import calculate_distances
from src.aoc2025.solvers.day08.input_parsing import parse_input


def solve(problem_input, num_connections=1000):
    boxes = parse_input(problem_input)

    # Compute distances
    distances = calculate_distances(boxes)
    sorted_distances = list(sorted(distances, key=lambda d: d.value))

    # Prepare forest
    forest = DisjointSetForest(len(boxes))

    # Connect boxes
    for i in range(0, num_connections):
        boxes_to_connect = list(sorted_distances[i].boxes)
        forest.merge(boxes_to_connect[0], boxes_to_connect[1])

    # Find sizes of circuits
    circuit_sizes = {}
    for i in range(0, len(boxes)):
        circuit_id = forest.find(i)
        if circuit_id not in circuit_sizes:
            circuit_sizes[circuit_id] = 0
        circuit_sizes[circuit_id] += 1

    three_largest_circuit_sizes = sorted(circuit_sizes.values(), reverse=True)[:3]

    return (
        three_largest_circuit_sizes[0]
        * three_largest_circuit_sizes[1]
        * three_largest_circuit_sizes[2]
    )
