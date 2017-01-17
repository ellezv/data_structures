"""Test file for binary search tree."""


import pytest


BREADTH_FIRST = [
    [[20, 9, 22, 7, 12, 21, 25], [20, 9, 22, 7, 12, 21, 25]],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], [10, 1, 13, 4, 32, 45, 3, 5, 34, 46]],
    [[1, 2, 3, 1.5, .5, .75, .25], [1, .5, 2, .25, .75, 1.5, 3]],
    [[10], [10]],
    [[], None],
]


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
    assert pop_bst.size() == 3


def test_size_for_empty_bst(empty_bst):
    """Test that the proper size is returned."""
    assert empty_bst.size() == 0


def test_depth_for_populated_bst(pop_bst):
    """Test that the depth returned is the number of layers in the bst."""
    assert pop_bst.depth() == 1


def test_depth_for_only_root_node(empty_bst):
    """Test that the root node has a bepth of 0."""
    empty_bst.insert(1)
    assert empty_bst.depth() == 0


def test_contains_value_in_tree(pop_bst):
    """Test contains method returns true if value is in tree."""
    assert pop_bst.contains(15)


def test_contains_value_not_in_tree(pop_bst):
    """Test contains method returns false if value not in tree."""
    assert not pop_bst.contains(42)


def test_balance_balanced_tree(pop_bst):
    """Return 0 for a balances bst."""
    assert pop_bst.balance() == 0


def test_balance_off_balance_left(pop_bst):
    """Return -1 for a bst with one more node on the left than the right."""
    pop_bst.insert(7)
    assert pop_bst.balance() == -1


def test_balance_off_balance_right(pop_bst):
    """Return 1 for a bst with one more node on the right than the left."""
    pop_bst.insert(13)
    assert pop_bst.balance() == 1


@pytest.mark.paramatrize('inserts, answer', BREADTH_FIRST)
def test_breadth_first(empty_bst, inserts, answer):
    """Test that breadth first returns the proper list."""
    for i in inserts:
        empty_bst.insert(i)
    assert empty_bst.breadth_first() is answer


def test_depth_empty_bst_raise_error(empty_bst):
    """Test that the proper error is raised."""
    message = "The tree is empty, it has no depth."
    with pytest.raises(AttributeError, message=message):
        empty_bst.depth()
