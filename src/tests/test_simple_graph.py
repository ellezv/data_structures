"""Test for our simple graph module."""

import pytest

@pytest.fixture
def empty_graph():
    "Instantiate an empty graph."
    from simple_graph import Graph
    g = Graph()
    return g


def test_init_graph_is_empty():
    """Check that new graph is empty."""
    from simple_graph import Graph
    graph = Graph()
    assert graph.nodes == {}


def test_add_node_empty_graph(empty_graph):
    """Add a node to an empty graph."""
    empty_graph.add_node("node")
    assert empty_graph.nodes["node"] == []


def test_add_already_existent_node_raise_error(empty_graph):
    """Add a node already in the graph raises correct error."""
    empty_graph.add_node("node")
    with pytest.raises(ValueError):
        empty_graph.add_node("node")
