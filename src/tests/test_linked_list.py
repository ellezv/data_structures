"""Tests for our linked_list module."""

import pytest


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


def test_pop_empty_linked_list():
    """Test pop method in our LinkedList class wit empty list."""
    from linked_list import LinkedList
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.pop()


def test_pop_linked():
    """Test pop method on populated linked list."""
    from linked_list import LinkedList
    lst = LinkedList([1, 2, 3, 4, 5])
    assert lst.pop() == 5


def test_size():
    """Test size method on LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    lst.push(3)
    lst.push(4)
    assert lst.size() == 3


def test_size_empty():
    """Test size method for empty linked list."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.size() == 0


def test_size_one():
    """Test size method for list with one node."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(4)
    assert lst.size() == 1


def test_search_linked_list_empty():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.search(2) is None


def test_search_linked_list_single():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(3)
    assert lst.search(3) is not None


def test_search_linked_list_multi():
    """Test search method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(1)
    lst.push(2)
    lst.push(3)
    assert lst.search(2) is not None


def test_remove_linked_list_single():
    """Test remove method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    lst.remove(2)
    assert lst.size() == 0


def test_remove_linked_list_multi():
    """Test remove method in our LinkedList class."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(5)
    lst.push(2)
    lst.remove(2)
    assert lst.size() == 1


def tests_display_empty():
    """Test display method for empty linked list."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.display() == "()"


def tests_display_one():
    """Test display method for list with one node."""
    from linked_list import LinkedList
    lst = LinkedList()
    lst.push(2)
    assert lst.display() == "(2)"
