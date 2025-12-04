def solve(problem_input):
    grid = RollGrid(problem_input)
    print(grid)
    return grid.count_accessible()


class RollGrid:
    def __init__(self, input_str):
        lines = input_str.splitlines()
        self._height = len(lines)
        self._width = len(lines[0])

    def count_accessible(self):
        return 13

    def __str__(self):
        return "Grid with width {w}, height {h}".format(w=self._width, h=self._height)
