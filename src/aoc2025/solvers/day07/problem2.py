from src.aoc2025.solvers.day07.input_parsing import parse_input


def solve(problem_input):
    manifold = parse_input(problem_input)
    timelines = {manifold.starting_point: 1}

    for splitter_row in manifold.splitter_rows:
        timelines = _do_splits(timelines, splitter_row)

    return sum(timelines.values())


def _do_splits(timelines, splitter_row):
    new_timelines = {}
    for beam in timelines.keys():
        if beam in splitter_row:
            _add_timelines(new_timelines, beam - 1, timelines[beam])
            _add_timelines(new_timelines, beam + 1, timelines[beam])
        else:
            _add_timelines(new_timelines, beam, timelines[beam])
    return new_timelines


def _add_timelines(timelines, position, how_many):
    if position not in timelines:
        timelines[position] = 0
    timelines[position] += how_many
