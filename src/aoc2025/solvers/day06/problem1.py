import re


def solve(problem_input):
    lines = parse_input(problem_input)

    result = 0
    for i in range(0, len(lines[0])):
        operators = []
        for line_num in range(0, len(lines) - 1):
            operators.append(int(lines[line_num][i]))
        symbol = lines[-1][i]
        if symbol == "+":
            result += sum(operators)
        else:
            result += mul(operators)

    return result


def mul(operators):
    result = 1
    for operator in operators:
        result *= operator
    return result


def parse_input(problem_input):
    return list(map(lambda l: _split_line(l), problem_input.splitlines()))


def _split_line(l):
    return re.split(r" +", l.strip())
