"""Tests for our dll module."""

import pytest


@pytest.fixture
def new_dll():
    """Init a new doubly linked list, push values and return the dll."""
    from dll import DbLinkedList
    dll = DbLinkedList(5)
    dll.push(4)
    dll.push(3)
    return dll


def test_init_empty_node():
    """Test a new empty node is None."""
    from dll import Node
    new_node = Node()
    assert new_node.value is None


def test_init_node():
    """Test a new node with value has correct value."""
    from dll import Node
    new_node = Node(5)
    assert new_node.value == 5


def test_init_dll():
    """Test a new empty dll is empty."""
    from dll import DbLinkedList
    new_dll = DbLinkedList()
    assert new_dll.head is None and new_dll.tail is None


def test_push_value_in_not_empty_list():
    """Test pushed value is the new head value."""
    from dll import DbLinkedList
    new_dll = DbLinkedList(5)
    new_dll.push(3)
    assert new_dll.head.value == 3


def test_tail_after_push_in_list(new_dll):
    """Test the tail is correct after push."""
    assert new_dll.tail.value == 5


def test_tail_after_append_in_list(new_dll):
    """Test the tail value changes after appending to dll."""
    new_dll.append(6)
    assert new_dll.tail.value == 6


def test_head_after_append_in_list(new_dll):
    """Test the the head stays the same after appending."""
    new_dll.append(6)
    assert new_dll.head.value == 3


def test_pop_empty_list():
    """Test popping from empty list correct raise error."""
    from dll import DbLinkedList
    dll = DbLinkedList()
    msg = "Cannot pop from an empty list"
    with pytest.raises(ValueError, message=msg):
        dll.pop()


def test_pop_returns_value(new_dll):
    """Test pop function will return the value popped."""
    assert new_dll.pop() == 3


def test_pop_sets_new_head(new_dll):
    """Test pop will set previous head next as new head value."""
    new_dll.pop()
    assert new_dll.head.value == 4


def test_pop_sets_new_head_previous(new_dll):
    """Test pop will set new head previous value to none."""
    new_dll.pop()
    assert new_dll.head.previous is None


def test_pop_sets_new_head_next(new_dll):
    """Test pop will set accurate head.next.value."""
    new_dll.pop()
    assert new_dll.head.next.value == 5


def test_shift_from_empty_list():
    """Test shifting from empty list will raise proper error."""
    from dll import DbLinkedList
    dll = DbLinkedList()
    msg = "Cannot shift from an empty list"
    with pytest.raises(ValueError, message=msg):
        dll.shift()


def test_shift_returns_value(new_dll):
    """Test shift will return shifted value."""
    assert new_dll.shift() == 5


def test_shift_sets_new_tail_is_previous(new_dll):
    """Test shift will set new tail value."""
    new_dll.shift()
    assert new_dll.tail.value == 4


def shift_sets_new_tail_next(new_dll):
    """Test shift will set new tail next value to None."""
    new_dll.shift()
    assert new_dll.tail.next is None


def test_remove_from_empty_list():
    """Test remove from empty dll raises appropriate error."""
    from dll import DbLinkedList
    dll = DbLinkedList()
    with pytest.raises(ValueError, message="Cannot remove from an empty list"):
        dll.remove(5)


def test_remove_returns_value(new_dll):
    """Test remove returns the correct value."""
    new_dll.remove(4) == 4
