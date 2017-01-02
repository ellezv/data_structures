"""Test for our simple graph module."""

import pytest


@pytest.fixture
def empty_graph():
    """Instantiate an empty graph."""
    from simple_graph import Graph
    g = Graph()
    return g


@pytest.fixture
def graph_no_edge(empty_graph):
    """Instantiate a graphe with nodes and no edge."""
    empty_graph.add_node("a")
    empty_graph.add_node("b")
    empty_graph.add_node("c")
    return empty_graph


@pytest.fixture
def full_graph(empty_graph):
    """Instantiate a graph with nodes and edges."""
    empty_graph.add_node("a")
    empty_graph.add_node("b")
    empty_graph.add_node("c")
    empty_graph.add_edge("a", "b")
    empty_graph.add_edge("a", "c")
    empty_graph.add_edge("b", "c")
    return empty_graph


def test_init_graph_is_empty():
    """Check that new graph is empty."""
    from simple_graph import Graph
    graph = Graph()
    assert graph._nodes == {}


def test_add_node_empty_graph(empty_graph):
    """Add a node to an empty graph."""
    empty_graph.add_node("node")
    assert empty_graph._nodes["node"] == []


def test_add_already_existent_node_raise_error(empty_graph):
    """Add a node already in the graph raises correct error."""
    empty_graph.add_node("node")
    with pytest.raises(ValueError, message="Node already present in Graph."):
        empty_graph.add_node("node")


def test_add_edge_on_empty_graph(empty_graph):
    """Add a new edge to an empty graph adds two new nodes and one edge."""
    empty_graph.add_edge("n1", "n2")
    assert empty_graph._nodes["n1"] == ["n2"]
    assert empty_graph._nodes["n2"] == []


def test_add_edge_on_full_graph(full_graph):
    """Add a new edge to full graph adds new edge."""
    full_graph.add_edge("c", "a")
    assert full_graph._nodes["c"] == ["a"]


def test_add_existing_edge_raises_error(full_graph):
    """Adding an existing edge raises expected error."""
    with pytest.raises(ValueError, message="This edge already exist."):
        full_graph.add_edge("a", "b")


def test_nodes_empty_graph(empty_graph):
    """The nodes method returns an empty list for an empty graph."""
    assert empty_graph.nodes() == []


def test_nodes_full_graph(full_graph):
    """The nodes method returns list of nodes on graph with nodes."""
    assert sorted(full_graph.nodes()) == ["a", "b", "c"]


def test_edges_on_graph_without_edges(empty_graph):
    """The edges method returns an empty list on an empty graph."""
    assert empty_graph.edges() == []


def test_edges_on_full_graph(full_graph):
    """The edges method returns a list of edges on graph with edges."""
    assert sorted(full_graph.edges()) == [("a", ["b", "c"]), ("b", ["c"])]


def test_del_existing_node(graph_no_edge):
    """Del_node delete the node."""
    graph_no_edge.del_node("a")
    assert sorted(graph_no_edge.nodes()) == ["b", "c"]


def test_del_node_not_in_graph_raises_error(graph_no_edge):
    """Del_node will raise error if node does not exist."""
    with pytest.raises(ValueError, message="This node is not in the graph"):
        graph_no_edge.del_node("I'm hungry")


def test_del_edge_not_in_graph_raises_error(graph_no_edge):
    """Del_edge will raise error if edge does not exist."""
    with pytest.raises(ValueError, message="This edge does not exist."):
        graph_no_edge.del_edge("a", "b")


def test_del_edge(full_graph):
    """Del_edge deletes existing edge in graph."""
    full_graph.del_edge("b", "c")
    assert full_graph.edges() == [("a", ["b", "c"])]
