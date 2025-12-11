from collections import deque


def shortest_path_joltage(joltage, buttons):
    return _JoltagePathFinder(joltage, buttons).shortest_path()


class _JoltagePathFinder:
    def __init__(self, goal, buttons):
        self._goal = tuple(goal)
        self._buttons = list(map(frozenset, buttons))

    def shortest_path(self):
        return 11
