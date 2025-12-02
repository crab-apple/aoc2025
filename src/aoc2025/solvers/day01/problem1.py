from aoc2025.solvers.day01.dial import Dial


def solve(problem_input):

    dial = Dial()
    dial.rotate("R", 50)
    times_at_0 = 0

    for line in problem_input.splitlines():
        direction = line[0]
        steps = int(line[1:])

        dial.rotate(direction, steps)

        if dial.pointer() == 0:
            times_at_0 += 1

    return times_at_0
