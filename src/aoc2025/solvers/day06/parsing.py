from src.aoc2025.solvers.day06.operation import Operation


def find_whitespace(line):
    result = set()
    for i in range(0, len(line)):
        if line[i] == " ":
            result.add(i)
    return result


def find_breakpoints(problem_input):
    lines = problem_input.splitlines()

    # For sanity, verify that all lines have the same length
    lengths = set(map(lambda l: len(l), lines))
    if len(lengths) != 1:
        raise Exception("Not all lines have the same length")

    result = find_whitespace(lines[0])
    for line in lines[1:]:
        result = result.intersection(find_whitespace(line))

    return list(sorted(result))


def parse_input(problem_input):
    lines = problem_input.splitlines()
    line_len = len(lines[0])
    breakpoints = list(reversed(find_breakpoints(problem_input)))

    breakpoints.append(-1)

    result = []

    while breakpoints:
        current = breakpoints.pop()
        next = breakpoints[-1] if breakpoints else line_len
        chunks = list(map(lambda l: l[current + 1 : next], lines))
        operands = chunks[0:-1]
        operator = chunks[-1].strip()
        result.append(Operation(operands, operator))
    return result
