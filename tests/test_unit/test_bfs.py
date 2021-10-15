import unittest
from scripts.url_parser.bfs import bfsearch
from collections import deque


class TestBFSAlgo(unittest.TestCase):

    def test_algo(self):

        adj_list = {}

        root_node_ = 'https://google.com'
        q_ = deque()
        max_level_ = 1

        bfsearch(adj_list, root_node_, q_, max_level_)
        self.assertTrue(len(adj_list))


if __name__ == '__main__':
    unittest.main()
