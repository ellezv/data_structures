"""An implementation of a simple graph in Python."""


class Graph(object):
    """A graph containing nodes and single-directional edges between them.

    g.nodes(): return a list of all nodes in the graph

    g.edges(): return a list of all edges in the graph

    g.add_node(n): adds a new node 'n' to the graph

    g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2',
    if either n1 or n2 are not already present in the graph, they should be added.

    g.del_node(n): deletes the node 'n' from the graph,
    raises an error if no such node exists.

    g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph,
    raises an error if no such edge exists

    g.has_node(n): True if node 'n' is contained in the graph, False if not.

    g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
    raises an error if n is not in g

    g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
    False if not, raises an error if either of the supplied nodes are not in g
    """

    def __init__(self):
        """Initialize an empty graph."""
        self._nodes = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return list(self._nodes)

    def edges(self):
        """Return a list of tuples with key and its list of edges."""
        tup_lst = []
        if self.nodes:
            for start in self._nodes:
                for end in self._nodes[start]:
                    tup_lst.append((start, end))
        return tup_lst

    def add_node(self, node):
        """Add a new node to the graph."""
        if node in self._nodes.keys():
            raise ValueError("Node already present in Graph.")
        else:
            self._nodes[node] = []

    def add_edge(self, n1, n2, weight=1):
        """Add a single-directional edge connecting n1 to n2."""
        self._nodes.setdefault(n1, [])
        self._nodes.setdefault(n2, [])
        for each in self._nodes[n1]:
            if n2 in each:
                self._nodes[n1].remove(each)
                break
        self._nodes[n1].append((n2, weight))

    def del_node(self, node):
        """Delete a given node from the graph."""
        if node in self._nodes.keys():
            del self._nodes[node]
            for each in self.edges():
                if each[1][0] == node:
                    self.del_edge(each[0], each[1])
        else:
            raise ValueError("This node is not in the graph")

    def del_edge(self, n1, n2):
        """Delete a given edge from the graph."""
        if n1 in self._nodes.keys() and n2 in self._nodes[n1]:
            self._nodes[n1].remove(n2)
        else:
            raise ValueError("This edge does not exist.")

    def has_node(self, node):
        """Return true is node is in graph, false if not."""
        return node in self._nodes

    def neighbors(self, node):
        """Return list of edges of the node given."""
        if node in self._nodes.keys():
            return self._nodes[node]
        raise ValueError("Node is not in graph.")

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 to n2 False if not."""
        if not self.has_node(n1) or not self.has_node(n2):
            raise KeyError
        if n2 in self._nodes[n1]:
            return True
        return False

    def depth_first_traversal(self, start, prev=None):
        """Return full depth-first traversal path of the graph."""
        if start not in self._nodes.keys():
            raise KeyError
        if prev is None:
            prev = []
        if start in prev:
            return []
        path_list = [start]
        nodes = []
        for each in self._nodes[start]:
            nodes.append(each[0])
        prev.append(start)
        for node in nodes:
            path_list.extend(self.depth_first_traversal(node, prev))
        return path_list

    def breadth_first_traversal(self, parent, path_list=None):
        """Return a list containing the nodes of the graph in order of breadth-first traversal."""
        if path_list is None:
            path_list = []
        if not isinstance(parent, list):
            path_list.append(parent)
            parent = [parent]
        children = []
        for item in parent:
            if self._nodes[item]:
                for edge in self._nodes[item]:
                    if edge[0] not in path_list:
                        children.append(edge[0])
        path_list.extend(children)
        if len(children) == 0:
            return path_list
        return self.breadth_first_traversal(children, path_list)


    def djikstras_shortest_path(self, start_node, dest_node):
        """Return the minimum distance between a start node
        and a destination node, and the path of minimum distance
        between those nodes."""
        unvisited = self.depth_first_traversal(start_node)

        if dest_node not in unvisited:
            raise ValueError("No path from start node to destination node.")

        distances_and_paths = {i: [None, [None]] for i in unvisited}
        distances_and_paths[start_node] = [0, [start_node]]
        current_node = start_node

        while True:
            for item in self.neighbors(current_node):
                study_node = item[0]
                current_node_distance = (distances_and_paths[current_node])[0]
                potential_distance = item[1] + current_node_distance
                original_distance = (distances_and_paths[study_node])[0]

                if study_node not in unvisited:
                    continue
                elif original_distance is None:
                    current_node_path = (distances_and_paths[current_node])[1][:]

                    current_node_path.append(item[0])

                    (distances_and_paths[item[0]])[0] = item[1] + current_node_distance
                    (distances_and_paths[item[0]])[1] = current_node_path

                    continue
                elif potential_distance < original_distance:
                    current_node_path = (distances_and_paths[current_node])[1][:]

                    current_node_path.append(item[0])

                    (distances_and_paths[item[0]])[0] = item[1] + current_node_distance
                    (distances_and_paths[item[0]])[1] = current_node_path

            if current_node == dest_node:

                return str((distances_and_paths[dest_node])[0]) + ' ' + str((distances_and_paths[dest_node])[1])

            unvisited.remove(current_node)
            next_node = None
            for key, value in distances_and_paths.items():
                if key in unvisited:
                    if next_node is None:
                        next_node = key
                        continue
                    elif (distances_and_paths[key])[0]:
                        if (distances_and_paths[key])[0] < (distances_and_paths[next_node])[0]:
                            next_node = key

            find_next_node()

            def find_next_node():
                """Find the next node whose neighbors will be studied."""
                next_node = None
                for key, value in distances_and_paths.items():
                    if key in unvisited:
                        if next_node is None:
                            next_node = key
                            continue
                        elif (distances_and_paths[key])[0]:
                            if (distances_and_paths[key])[0] < (distances_and_paths[next_node])[0]:
                                next_node = key
                current_node = next_node




# if __name__ == "__main__": # pragma: no cover
#     import timeit

#     def fill_graph(graph):
#         for i in range(100):
#             graph.add_edge(i, i + 1)

#     def fill_and_depth_trav():
#         g = Graph()
#         fill_graph(g)
#         g.depth_first_traversal(1)

#     def fill_and_breadth_trav():
#         g = Graph()
#         fill_graph(g)
#         g.breadth_first_traversal(1)

#     depth_trav_timed = timeit.repeat(stmt="fill_and_depth_trav()", setup="from __main__ import fill_and_depth_trav", number=1000, repeat=3)
#     breadth_trav_timed = timeit.repeat(stmt="fill_and_breadth_trav()", setup="from __main__ import fill_and_breadth_trav", number=1000, repeat=3)
#     average_depth_timed = float(sum(depth_trav_timed) / len(depth_trav_timed))
#     average_breadth_timed = float(sum(breadth_trav_timed) / len(breadth_trav_timed))

#     print("Depth traversal times:", depth_trav_timed)
#     print("average:", average_depth_timed)
#     print("Breadth traversal times:", breadth_trav_timed)
#     print("average:", average_breadth_timed)
#     print("This print statement was brought to you by Ben and Maelle. You're welcome.")
