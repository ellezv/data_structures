"""Tests for our dll module."""

import pytest


@pytest.fixture
def new_dll():
    from dll import DbLinkedList
    dll = DbLinkedList(5)
    dll.push(4)
    dll.push(3)
    return dll


def test_init_empty_node():
    from dll import Node
    new_node = Node()
    assert new_node.value is None


def test_init_node():
    from dll import Node
    new_node = Node(5)
    assert new_node.value == 5


def test_init_dll():
    from dll import DbLinkedList
    new_dll = DbLinkedList()
    assert new_dll.head is None and new_dll.tail is None


def test_push_value_in_not_empty_list():
    from dll import DbLinkedList
    new_dll = DbLinkedList(5)
    new_dll.push(3)
    assert new_dll.head.value == 3


def test_tail_after_push_in_list(new_dll):
    assert new_dll.tail.value == 5


def test_tail_after_append_in_list(new_dll):
    new_dll.append(6)
    assert new_dll.tail.value == 6


def test_head_after_append_in_list(new_dll):
    new_dll.append(6)
    assert new_dll.head.value == 3


def test_pop_empty_list():
    from dll import DbLinkedList
    dll = DbLinkedList()
    msg = "Cannot pop from an empty list"
    with pytest.raises(ValueError, message=msg):
        dll.pop()


def test_pop_returns_value(new_dll):
    assert new_dll.pop() == 3


def test_pop_sets_new_head(new_dll):
    new_dll.pop()
    assert new_dll.head.value == 4