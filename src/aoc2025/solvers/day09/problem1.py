def solve(problem_input):
    tiles = _parse_tiles(problem_input)

    max_area = 0
    for i in range(0, len(tiles)):
        for j in range(i + 1, len(tiles)):
            max_area = max(max_area, _area_between(tiles[i], tiles[j]))

    return max_area


def _parse_tiles(problem_input):
    result = []
    for line in problem_input.splitlines():
        chunks = line.split(",")
        tile = list(map(int, chunks))
        result.append(tile)
    return result


def _area_between(tile_a, tile_b):
    return (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
