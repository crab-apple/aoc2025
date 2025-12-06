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
