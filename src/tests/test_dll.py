"""Tests for our dll module."""


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


def test_push_value_in_not_empty_list():
    from dll import DbLinkedList
    new_dll = DbLinkedList(5)
    new_dll.push(3)
    assert new_dll.tail.value == 5

