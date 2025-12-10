from collections import deque


def shortest_path(goal, buttons):
    goal = frozenset(goal)
    buttons = list(map(frozenset, buttons))

    start = frozenset()
    pending = deque()

    if start == goal:
        return 0

    graph = {start: 0}
    pending.append(start)

    while pending:
        current_node = pending.popleft()
        current_node_cost = graph[current_node]
        for button in buttons:
            next_node = current_node.symmetric_difference(button)
            next_node_cost = current_node_cost + 1
            if next_node == goal:
                return next_node_cost

    raise Exception("Destination not found")
