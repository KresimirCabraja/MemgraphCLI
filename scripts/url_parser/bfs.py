import collections
import logging
from utils.request_helpers import get_webpage, clear_links
from typing import Deque


def bfsearch(adj_list: dict, root_node: str, q: Deque, max_level: int):

    level = 0
    logging.info(f'Current parsing level is: {level}')
    q.append(root_node)
    visited_nodes = set()
    visited_nodes.add(root_node)
    logging.info(f'Starting to parse {root_node}')
    while q:

        level_size = len(q)

        for i in range(level_size):
            s = q.popleft()
            response = get_webpage(s)
            child_nodes = clear_links(response)
            adj_list[s] = child_nodes

            for child in child_nodes:
                if child not in visited_nodes and not None:
                    visited_nodes.add(child)
                    q.append(child)

        if level == max_level:
            return
        level += 1
        logging.info(f'New parsing level is: {level}')


if __name__ == '__main__':

    adj_list_ = {}
    root_node_ = 'https://google.com'
    q_ = collections.deque()
    max_level_ = 1

    bfsearch(adj_list_, root_node_, q_, max_level_)
