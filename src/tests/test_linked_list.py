"""Tests for our linked_list module."""


def test_linked_list():
    """Test the instantiation of our Linked List."""
    from linked_list import LinkedList
    lst = LinkedList()
    if lst.head is None:
        pass


def test_node():
    """Test the instantiation of a node."""
    from linked_list import Node
    new_node = Node(1, 2)
    assert new_node.value == 1 and new_node.next == 2


def test_push_linked_list():
    """Test the push method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    assert lst.head.value == 2
