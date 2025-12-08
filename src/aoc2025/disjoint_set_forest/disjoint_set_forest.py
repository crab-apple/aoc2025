class DisjointSetForest:
    def __init__(self, size):
        self._nodes = []
        for i in range(0, size):
            self._nodes.append(i)

    def find(self, i):
        parent = self._nodes[i]
        if parent == i:
            return i
        root = self.find(parent)
        self._nodes[i] = root
        return root

    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self._nodes[root_a] = root_b
