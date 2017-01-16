"""Test file for binary search tree."""


import pytest


@pytest.fixture
def empty_bst():
    """Instantiate empty bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree()
    return bst


@pytest.fixture
def pop_bst():
    """Instantiate a populated bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(5)
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


def test_insert_existing_value(empty_bst):
    """Test that an existing value is ignored."""
    empty_bst.insert(1)
    assert empty_bst.insert(1) == 1
    assert len(empty_bst._values.keys()) == 1


def test_insert_for_larger_tree(pop_bst):
    """Test insert for a larger tree."""
    pop_bst.insert(3)
    assert pop_bst._root_node.left.left.value == 3


def test_search_existing_node(pop_bst):
    """Test that the search method finds the desired node."""
    assert pop_bst.search(5) == pop_bst._values[5]
    assert pop_bst.search(5).value == 5


def test_search_non_existing_node(pop_bst):
    """Test that the search method returns None if the node does not exist."""
    assert pop_bst.search(7) is None

def test_size_for_populated_bst(pop_bst):
    """Test that the proper size is returned."""