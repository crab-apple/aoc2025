def parse_tiles(problem_input):
    result = []
    for line in problem_input.splitlines():
        chunks = line.split(",")
        tile = list(map(int, chunks))
        result.append(tile)
    return result


def area_between(tile_a, tile_b):
    return (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)


def determine_turn_direction(tile_prev, tile_this, tile_next):
    directions = (_determine_direction(tile_prev, tile_this), _determine_direction(tile_this, tile_next))
    match directions:
        case ("N", "E"):
            return "R"
        case ("N", "W"):
            return "L"
        case ("S", "E"):
            return "L"
        case ("S", "W"):
            return "R"
        case ("E", "N"):
            return "L"
        case ("E", "S"):
            return "R"
        case ("W", "N"):
            return "R"
        case ("W", "S"):
            return "L"

    raise ValueError()


def _determine_direction(tile_a, tile_b):
    if tile_a[0] == tile_b[0] and tile_a[1] == tile_b[1]:
        raise ValueError("Same tile")
    if tile_a[0] != tile_b[0] and tile_a[1] != tile_b[1]:
        raise ValueError("Tiles not aligned")
    if tile_a[0] == tile_b[0] and tile_a[1] > tile_b[1]:
        return "N"
    elif tile_a[0] == tile_b[0]:
        return "S"
    elif tile_a[0] > tile_b[0]:
        return "W"
    else:
        return "E"
