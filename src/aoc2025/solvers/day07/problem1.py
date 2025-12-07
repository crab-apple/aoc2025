from src.aoc2025.solvers.day07.input_parsing import parse_input


def solve(problem_input):
    manifold = parse_input(problem_input)
    beams = {manifold.starting_point}
    result = 0
    for splitter_row in manifold.splitter_rows:
        beams, num_splits = _do_splits(beams, splitter_row)
        result += num_splits

    return result


def _do_splits(beams, splitter_row):
    num_splits = 0
    beams_after = set()
    for beam in beams:
        if beam in splitter_row:
            num_splits += 1
            beams_after.add(beam - 1)
            beams_after.add(beam + 1)
        else:
            beams_after.add(beam)

    return beams_after, num_splits
