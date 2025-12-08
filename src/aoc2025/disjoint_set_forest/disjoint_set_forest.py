class DisjointSetForest:
    def __init__(self, size):
        self._nodes = []
        for i in range(0, size):
            self._nodes.append(i)

    def find(self, i):
        return i if self._nodes[i] == i else self.find(self._nodes[i])

    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self._nodes[root_a] = root_b
