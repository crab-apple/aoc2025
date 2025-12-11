from collections import namedtuple


def solve(problem_input):
    output_graph = _parse_input(problem_input)

    input_graph = {}
    for device in output_graph:
        for output in output_graph[device]:
            if output not in input_graph:
                input_graph[output] = set()
            input_graph[output].add(device)

    result = _count_paths("out", input_graph)

    return result.both


def _count_paths(destination, input_graph):
    cache = {}
    return _count_paths_memoized(destination, input_graph, cache)


def _count_paths_memoized(destination, input_graph, cache):
    if destination == "svr":
        return PathCount(dac=0, fft=0, both=0, none=1)
    if destination not in input_graph:
        return PathCount(dac=0, fft=0, both=0, none=0)
    if destination in cache:
        return cache[destination]

    result = PathCount(0, 0, 0, 0)
    for input in input_graph[destination]:
        upstream = _count_paths_memoized(input, input_graph, cache)
        result = PathCount(
            dac=result.dac + upstream.dac,
            fft=result.fft + upstream.fft,
            both=result.both + upstream.both,
            none=result.none + upstream.none,
        )

    if destination == "dac":
        result = PathCount(dac=result.none, fft=0, both=result.fft, none=0)

    if destination == "fft":
        result = PathCount(dac=0, fft=result.none, both=result.dac, none=0)

    cache[destination] = result
    return result


def _parse_input(problem_input):
    graph = {}
    for line in problem_input.splitlines():
        device = line.split(":")[0]
        outputs = set(line.split(":")[1].strip().split(" "))
        graph[device] = outputs
    return graph


PathCount = namedtuple("PathCount", field_names=["dac", "fft", "both", "none"])
