"""Test for priority queue module."""

import pytest


def test_insert():
    """Test insert tuple in a empty priority queue."""
    from priority_queue import PriorityQueue
    q = PriorityQueue()
    q.insert(('a', 1))
    assert q._container[1][0] == 'a'


def test_insert_none():
    """Test insert with no value in empty priority queue."""
    from priority_queue import PriorityQueue
    q = PriorityQueue()
    with pytest.raises(TypeError, message='Must insert with tuple!'):
        q.insert()


def test_init_wrong_value():
    """Test init a priority queue with wrong value raises expected error."""
    from priority_queue import PriorityQueue
    with pytest.raises(TypeError, message='Must initialize with tuple!'):
        PriorityQueue(5)
