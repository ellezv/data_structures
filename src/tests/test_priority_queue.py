"""Test for priority queue module."""

import pytest


@pytest.fixture
def new_pqueue():
    from priority_queue import PriorityQueue
    q = PriorityQueue()
    return q


def test_insert(new_pqueue):
    """Test insert tuple in a empty priority queue."""
    new_pqueue.insert(('a', 1))
    assert new_pqueue._container[1][0] == 'a'


def test_insert_none(new_pqueue):
    """Test insert with no value in empty priority queue."""
    with pytest.raises(AttributeError):
        new_pqueue.insert()


def test_insert_a_bunch(new_pqueue):
    """Test insert a lot of stuff."""
    new_pqueue.insert(1)
    new_pqueue.insert(2, -2)
    new_pqueue.insert(3, -3)
    new_pqueue._container = {-3: 3, -2: 2, 0: 1}
