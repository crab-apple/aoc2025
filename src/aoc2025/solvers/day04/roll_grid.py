class RollGrid:
    def __init__(self, input_str):
        self._lines = input_str.splitlines()
        self._height = len(self._lines)
        self._width = len(self._lines[0])
        self._memory = dict()
        self._accessible = set()
        self._init_memory()

    def _init_memory(self):
        for row_num in range(0, self._height):
            for col_num in range(0, self._width):
                surrounding_rolls = self._count_surrounding_rolls(row_num, col_num)
                self._memory[(row_num, col_num)] = surrounding_rolls
                if surrounding_rolls < 4:
                    self._accessible.add((row_num, col_num))

    def count_accessible(self):
        count = 0
        for row_num in range(0, self._height):
            for col_num in range(0, self._width):
                if self._is_roll(row_num, col_num) and self._is_accessible(
                    row_num, col_num
                ):
                    count += 1
        # return 13
        return count

    def __str__(self):
        return "Grid with width {w}, height {h}".format(w=self._width, h=self._height)

    def _is_accessible(self, row_num, col_num):
        return self._count_surrounding_rolls(row_num, col_num) < 4

    def _is_roll(self, row_num, col_num):
        return self._lines[row_num][col_num] == "@"

    def _is_in_grid(self, row_num, col_num):
        return 0 <= row_num < self._height and 0 <= col_num < self._width

    def _count_surrounding_rolls(self, row_num, col_num):
        count = 0
        for r in range(row_num - 1, row_num + 2):
            for c in range(col_num - 1, col_num + 2):
                if r == row_num and c == col_num:
                    continue
                if self._is_in_grid(r, c) and self._is_roll(r, c):
                    count += 1
        return count

    def remove_accessible(self):
        pass
