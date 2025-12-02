from aoc2025.solvers.day01.dial import Dial


def solve(problem_input):

    dial = Dial()
    dial.rotate("R", 50)
    clicks = 0

    for line in problem_input.splitlines():
        direction = line[0]
        steps = int(line[1:])

        clicks += dial.rotate(direction, steps)

    return clicks
