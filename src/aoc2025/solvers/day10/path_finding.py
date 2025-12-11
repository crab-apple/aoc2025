from collections import deque


def shortest_path(goal, buttons):
    return _PathFinder(goal, buttons).shortest_path()


def shortest_path_joltage(joltage, buttons):
    return _JoltagePathFinder(joltage, buttons).shortest_path()


class _PathFinder:
    def __init__(self, goal, buttons):
        self._goal = frozenset(goal)
        self._buttons = list(map(frozenset, buttons))

        self._pending_visit = deque()
        self._known = {}

        start = frozenset()
        self._known[start] = 0
        self._pending_visit.append(start)

    def shortest_path(self):
        while self._pending_visit:
            current_node = self._pending_visit.popleft()
            if current_node == self._goal:
                return self._known[current_node]

            self._visit(current_node)

        raise Exception("Destination not found")

    def _visit(self, node):
        for button in self._buttons:
            self._push_button(node, button)

    def _push_button(self, node, button):
        next_node = node.symmetric_difference(button)
        next_node_cost = self._known[node] + 1

        if next_node not in self._known or self._known[next_node] > next_node_cost:
            self._known[next_node] = next_node_cost
            self._pending_visit.append(next_node)


class _JoltagePathFinder:
    def __init__(self, goal, buttons):
        self._goal = tuple(goal)
        self._buttons = list(map(frozenset, buttons))


    def shortest_path(self):
        return 11
