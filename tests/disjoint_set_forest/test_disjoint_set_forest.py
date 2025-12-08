import random
import unittest

from src.aoc2025.disjoint_set_forest.disjoint_set_forest import DisjointSetForest


class TestDisjointSetForest(unittest.TestCase):

    def test_initially_every_node_in_its_own_set(self):
        forest = DisjointSetForest(10)

        for i in range(0, 10):
            self.assertEqual(i, forest.find(i))

    def test_merge_sets_of_one(self):
        forest = DisjointSetForest(10)

        forest.merge(1, 2)
        forest.merge(3, 4)

        self.assertEqual(forest.find(1), forest.find(2))
        self.assertEqual(forest.find(3), forest.find(4))
        self.assertNotEqual(forest.find(1), forest.find(3))

    def test_merge_larger_sets(self):
        forest = DisjointSetForest(10)

        forest.merge(1, 2)
        forest.merge(3, 4)
        forest.merge(1, 4)

        root = forest.find(1)
        self.assertEqual(root, forest.find(1))
        self.assertEqual(root, forest.find(2))
        self.assertEqual(root, forest.find(3))
        self.assertEqual(root, forest.find(4))

    def test_performance(self):
        size = 100000
        num_merges = 100000
        forest = DisjointSetForest(size)

        for i in range(0, num_merges):
            node_a = random.randrange(size)
            node_b = random.randrange(size)
            forest.merge(node_a, node_b)
