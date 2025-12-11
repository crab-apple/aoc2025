def solve(problem_input):
    output_graph = _parse_input(problem_input)

    input_graph = {}
    for device in output_graph:
        for output in output_graph[device]:
            if output not in input_graph:
                input_graph[output] = set()
            input_graph[output].add(device)

    result = _count_paths("out", input_graph)

    return result


def _count_paths(destination, input_graph):
    cache = {}
    return _count_paths_memoized(destination, input_graph, cache)


def _count_paths_memoized(destination, input_graph, cache):
    if destination == "you":
        return 1
    if destination not in input_graph:
        return 0
    if destination in cache:
        return cache[destination]

    result = 0
    for input in input_graph[destination]:
        result += _count_paths_memoized(input, input_graph, cache)
    cache[destination] = result
    return result


def _parse_input(problem_input):
    graph = {}
    for line in problem_input.splitlines():
        device = line.split(":")[0]
        outputs = set(line.split(":")[1].strip().split(" "))
        graph[device] = outputs
    return graph
