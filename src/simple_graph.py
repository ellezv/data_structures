"""An implementation of a simple graph in Python"""


class Graph(object):
    """A graph containing nodes and single-directional edges between them.
    g.nodes(): return a list of all nodes in the graph

    g.edges(): return a list of all edges in the graph

    g.add_node(n): adds a new node 'n' to the graph

    g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.

    g.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists

    g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists

    g.has_node(n): True if node 'n' is contained in the graph, False if not.

    g.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g

    g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
    """

    def __init__(self):
        """Initialize an empty graph."""
        self._nodes = {}

    def add_node(self, node):
        """Add a new node to the graph."""
        if node in self._nodes.keys():
            raise ValueError("Node already present in Graph.")
        else:
            self._nodes[node] = []

    def add_edge(self, n1, n2):
        """Add a single-directional edge connecting n1 to n2"""
        self._nodes.setdefault(n1, [])
        self._nodes.setdefault(n2, [])
        if n2 not in self._nodes[n1]:
            self._nodes[n1].append(n2)
        else:
            raise ValueError("This edge already exist.")
