"""Tests for our binheap module."""

def test_init_empty_node():
    from binheap import Node
    new_node = Node()
    assert new_node.value is None
    assert new_node.right is None
    assert new_node.left is None


def test_init_empty_binheap():
    from binheap import Binheap
    new_binheap = Binheap()
    assert new_binheap.top is None