from collections import namedtuple


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
                position = Position(row_num, col_num)
                if not self._is_roll(position):
                    continue
                surrounding_rolls = self._count_surrounding_rolls(position)
                self._memory[position] = surrounding_rolls
                if surrounding_rolls < 4:
                    self._accessible.add(position)

    def count_accessible(self):
        return len(self._accessible)

    def __str__(self):
        return "Grid with width {w}, height {h}".format(w=self._width, h=self._height)

    def print_grid(self):
        result = ""
        for row_num in range(0, self._height):
            for col_num in range(0, self._width):
                result += "@" if Position(row_num, col_num) in self._memory else "."
            result += "\n"
        return result

    def _is_roll(self, position):
        return self._lines[position.row_num][position.col_num] == "@"

    def _is_in_grid(self, position):
        return (
            0 <= position.row_num < self._height and 0 <= position.col_num < self._width
        )

    def _count_surrounding_rolls(self, position):
        count = 0

        for other_position in self._surrounding_positions(position):
            if self._is_roll(other_position):
                count += 1

        return count

    def remove_accessible(self):
        new_accessible = set()

        for accessible_roll in self._accessible:
            del self._memory[accessible_roll]

        for accessible_roll in self._accessible:
            for surrounding in self._surrounding_positions(accessible_roll):
                if not surrounding in self._memory:
                    continue
                self._memory[surrounding] -= 1
                if self._memory[surrounding] < 4:
                    new_accessible.add(surrounding)
        self._accessible.clear()
        self._accessible = new_accessible

    def _surrounding_positions(self, position):
        result = set()
        for r in range(position.row_num - 1, position.row_num + 2):
            for c in range(position.col_num - 1, position.col_num + 2):
                other_position = Position(r, c)
                if other_position == position:
                    continue
                if not self._is_in_grid(other_position):
                    continue
                result.add(other_position)
        return result


Position = namedtuple("Position", ["row_num", "col_num"])
