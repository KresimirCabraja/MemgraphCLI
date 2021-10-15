from typing import Generator


class ADJListToGraphNodesConverter:
    """Unpack ADJ_LIST
        from:
            { 'parent_node': [list, of, neighbours/children's]
        to:
            (parent_node, 'child[0]),
            (parent_node, 'child[1])'
            ...
    """
    def __init__(self, adj_list: dict):
        self.adj_list = adj_list
        self.nodes = []

    def __iterate_adj_list(self) -> None:
        """iterate over adj_list items and create nodes"""
        for i in self.adj_list.items():
            parent = i[0]
            for _ in i[-1]:
                self.nodes.append((parent, _))

    @property
    def get_nodes(self) -> Generator[tuple, None, None]:
        """Generator for returning list of nodes"""
        self.__iterate_adj_list()
        yield self.nodes
