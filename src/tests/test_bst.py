"""Test file for binary search tree."""


import pytest


BREADTH_FIRST = [
    [[20, 9, 22, 7, 12, 21, 25], [20, 9, 22, 7, 12, 21, 25]],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], [10, 1, 13, 4, 45, 3, 5, 32, 46, 34]],
    [[1, 2, 3, 1.5, .5, .75, .25], [1, .5, 2, .25, .75, 1.5, 3]],
    [[10], [10]],
    [[], []],
]

IN_ORDER = [
    [[], []],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], [1, 3, 4, 5, 10, 13, 32, 34, 45, 46]],
    [[20, 9, 22, 7, 12, 21, 25], [7, 9, 12, 20, 21, 22, 25]],
    [[10], [10]],
    [[1, 2, 3, 1.5, .5, .75, .25], [.25, .5, .75, 1, 1.5, 2, 3]]
]

POST_ORDER = [
    [[1, 2, 3, 1.5, .5, .75, .25], [0.25, 0.75, 0.5, 1.5, 3, 2, 1]],
    [[20, 9, 22, 7, 12, 21, 25], [7, 12, 9, 21, 25, 22, 20]],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], [3, 5, 4, 1, 34, 32, 46, 45, 13, 10]],
    [[9], [9]],
    [[], []]
]

PRE_ORDER = [
    [[1, 2, 3, 1.5, .5, .75, .25], [1, .5, .25, .75, 2, 1.5, 3]],
    [[20, 9, 22, 7, 12, 21, 25], [20, 9, 7, 12, 22, 21, 25]],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], [10, 1, 4, 3, 5, 13, 45, 32, 34, 46]],
    [[9], [9]],
    [[], []]
]

DELETE_SIZE = [
    [[1, 2, 3, 1.5, .5, .75, .25], 2, 6],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], 3, 9],
    [[2, 3, 1, 1.5], 1, 3],
    [[9], 9, 0],
    [[20, 9, 22, 7], 20, 3],
    [[2, 3, 1, 1.5, 4], 4, 4],
    [[10, 13, 45, 32, 46, 1, 34, 4, 3, 5], 1, 9],
    [[1, 3, 2, 6, 5, 4], 6, 5],

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


@pytest.mark.parametrize('inserts, answer', BREADTH_FIRST)
def test_breadth_first(empty_bst, inserts, answer):
    """Test that breadth first returns the proper list."""
    for i in inserts:
        empty_bst.insert(i)
    a = empty_bst.breadth_first()
    assert [next(a) for i in inserts] == answer


def test_depth_empty_bst_raise_error(empty_bst):
    """Test that the proper error is raised."""
    message = "The tree is empty, it has no depth."
    with pytest.raises(AttributeError, message=message):
        empty_bst.depth()


@pytest.mark.parametrize('inserts, answer', IN_ORDER)
def test_in_order(empty_bst, inserts, answer):
    """Test that in order traversal yield expected value."""
    for i in inserts:
        empty_bst.insert(i)
    a = empty_bst.in_order()
    assert [next(a) for i in inserts] == answer


@pytest.mark.parametrize('inserts, answer', POST_ORDER)
def test_post_order(empty_bst, inserts, answer):
    """Test that post order traversal yield expected value."""
    for i in inserts:
        empty_bst.insert(i)
    a = empty_bst.post_order()
    assert [next(a) for i in inserts] == answer


@pytest.mark.parametrize('inserts, answer', PRE_ORDER)
def test_pre_order(empty_bst, inserts, answer):
    """Test that pre order traversal yield expected value."""
    for i in inserts:
        empty_bst.insert(i)
    a = empty_bst.pre_order()
    assert [next(a) for i in inserts] == answer


def test_delete_unexisting_node(empty_bst):
    """Test delete on an empty tree."""
    message = "You can't delete a nonexistant node."
    with pytest.raises(ValueError, message=message):
        empty_bst.delete(1)


@pytest.mark.parametrize('inserts, node, size', DELETE_SIZE)
def test_delete_changes_size(empty_bst, inserts, node, size):
    """Test that delete a node will change the size."""
    for i in inserts:
        empty_bst.insert(i)
    empty_bst.delete(node)
    assert empty_bst.size() == size


def test_improper_delete(pop_bst):
    """Test for Joey's method which works anyway."""
    pop_bst._improper_delete(15)
    assert pop_bst.size() == 2
    assert pop_bst._root_node.value == 10
    assert pop_bst._root_node.left.value == 5
    assert pop_bst._root_node.right is None
