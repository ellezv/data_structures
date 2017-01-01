"""Test for our simple graph module."""


def test_init_graph_is_empty():
    from simple_graph import Graph
    graph = Graph()
    assert graph.nodes == {}