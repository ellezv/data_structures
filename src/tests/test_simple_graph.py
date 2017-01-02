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
    with pytest.raises(ValueError, message="This edge already exist."):
        full_graph.add_edge("a", "b")
