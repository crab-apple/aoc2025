from collections import namedtuple

TachyonManifold = namedtuple("TachyonManifold", ["starting_point", "splitter_rows"])


def parse_input(the_input):
    lines = the_input.splitlines()

    starting_point = lines[0].index("S")

    splitter_rows = list(map(lambda l: _find_splitters_in_line(l), lines[1:]))

    return TachyonManifold(starting_point, splitter_rows)


def _find_splitters_in_line(line):
    result = set()
    for i in range(0, len(line)):
        if line[i] == "^":
            result.add(i)
    return result
