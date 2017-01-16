"""Test file for binary search tree."""


import pytest


def test_init_bst():
    """Test that an instance of the binary search tree is properly made."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree()
    assert isinstance(bst, BinarySearchTree)


def test_init_node():
    """Test that an instance of a Node is properly made."""
    from binary_search_tree import Node
    node = Node(1)
    assert isinstance(node, Node)


def test_node_val():
    """Test the value of the Node."""
    from binary_search_tree import Node
    node = Node(1)
    assert Node.val = 1
