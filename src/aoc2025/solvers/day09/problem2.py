from src.aoc2025.solvers.day09.utils import determine_turn_direction, parse_tiles


def solve(problem_input):
    tiles = parse_tiles(problem_input)

    # Classify edges between r-turning and l-turning
    turns = []
    for i in range(0, len(tiles)):
        tile_this = tiles[i]
        tile_prev = tiles[i - 1]
        tile_next = tiles[(i + 1) % len(tiles)]
        turns.append(determine_turn_direction(tile_prev, tile_this, tile_next))

    # Count the number of turns either way to figure out the overall direction of the loop
    num_lefts = len(list(filter(lambda t: t == "L", turns)))
    num_rights = len(list(filter(lambda t: t == "R", turns)))
    if num_lefts == num_rights + 4:
        loop_direction = "L"
    elif num_rights == num_lefts + 4:
        loop_direction = "R"
    else:
        raise Exception

    # Based on the direction, re-classify edges as convex or concave
    for i in range(0, len(turns)):
        turns[i] = "CONVEX" if turns[i] == loop_direction else "CONCAVE"

    # Compute all areas
    # Sort by size descendant
    # For each one, figure out whether there's a concave edge in the rectangle
    #    (it must be fully in, being at the edge doesn't count)
    #    (to make this possible, it may be necessary to:
    #    * make a collection including the concave edges only
    #    * index by one of the two coordinates (tree-set or so)

    return 24
