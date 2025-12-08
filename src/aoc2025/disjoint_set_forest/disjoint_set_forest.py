class DisjointSetForest:
    def __init__(self, size):
        self._nodes = []
        for i in range(0, size):
            self._nodes.append(Node(i, 0))

    def find(self, i):
        parent = self._nodes[i].parent
        if parent == i:
            return i
        root = self.find(parent)
        self._nodes[i].parent = root
        return root

    def merge(self, a, b):
        root_node_a = self._nodes[self.find(a)]
        root_node_b = self._nodes[self.find(b)]

        if root_node_a.rank > root_node_b.rank:
            root_node_a, root_node_b = root_node_b, root_node_a

        root_node_a.parent = root_node_b.parent
        if root_node_a.rank == root_node_b.rank:
            root_node_a.parent = root_node_b.parent
            root_node_b.rank += 1


class Node:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank
