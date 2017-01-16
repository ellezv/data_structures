"""Test file for binary search tree."""


import pytest


@pytest.fixture
def empty_bst():
    """Instantiate empty bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree()
    return bst


def test_init_bst(empty_bst):
    """Test that an instance of the binary search tree is properly made."""
    from binary_search_tree import BinarySearchTree
    assert isinstance(empty_bst, BinarySearchTree)


def test_init_node():
    """Test that an instance of a Node is properly made."""
    from binary_search_tree import Node
    node = Node(1)
    assert isinstance(node, Node)


def test_node_val():
    """Test the value of the Node."""
    from binary_search_tree import Node
    node = Node(1)
    assert node.value == 1


def test_init_sets_root_to_none(empty_bst):
    """Test the root node is None."""
    assert empty_bst._root_node is None


def test_init_sets_empty_dict_values(empty_bst):
    """Test the values dict is empty."""
    assert empty_bst._values == {}


def test_insert_add_value_to_dict(empty_bst):
    """Test the value gets added to values dictionary."""
    empty_bst.insert(1)
    assert empty_bst._values[1]


def test_insert_value_empty_bst_set_root_node(empty_bst):
    """Test the root node is set to first inserted value."""
    empty_bst.insert(1)
    assert empty_bst._root_node.value == 1


def test_insert_right_node_added(empty_bst):
    """Test that a node of a higher value is added to the right of the root."""
    empty_bst.insert(1)
    empty_bst.insert(2)
    assert empty_bst._root_node.right.value is 2


def test_insert_left_node_added(empty_bst):
    """Test that a node of a lesser value is added tp the left of the root."""
    empty_bst.insert(1)
    empty_bst.insert(0)
    assert empty_bst._root_node.left.value is 0
