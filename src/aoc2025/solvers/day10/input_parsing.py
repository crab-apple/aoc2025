from collections import namedtuple


def parse_input(problem_input):
    result = []
    for line in problem_input.splitlines():
        result.append(_parse_machine(line))
    return result


def _parse_machine(line):
    chunks = line.split(" ")
    lights_str = chunks[0][1:-1]
    joltage_str = chunks[-1]
    button_strs = chunks[1:-1]

    lights = set(filter(lambda l: lights_str[l] == "#", range(0, len(lights_str))))

    buttons = []
    for button_str in button_strs:
        buttons.append(set(map(int, button_str[1:-1].split(","))))

    return Machine(lights, buttons)


Machine = namedtuple("Machine", ["goal", "buttons"])
