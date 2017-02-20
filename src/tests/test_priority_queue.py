"""Test for priority queue module."""

import pytest


@pytest.fixture
def new_pqueue():
    """Return empty priority queue."""
    from priority_queue import PriorityQueue
    q = PriorityQueue()
    return q


@pytest.fixture
def filled_pqueue():
    """Return filled priority queue."""
    from priority_queue import PriorityQueue
    q = PriorityQueue([(1, -1), (2, -2), (3, -3), (4, -4)])
    return q


def test_insert_on_empty(new_pqueue):
    """Test insert in a empty priority queue."""
    new_pqueue.insert('a', -1)
    assert new_pqueue._container[-1][0] == 'a'


def test_insert_none(new_pqueue):
    """Test insert with no value in empty priority queue."""
    with pytest.raises(TypeError):
        new_pqueue.insert()


def test_insert_a_bunch(new_pqueue):
    """Test insert a lot of stuff."""
    new_pqueue.insert(1)
    new_pqueue.insert(2, -2)
    new_pqueue.insert(3, -3)
    new_pqueue._container = {-3: 3, -2: 2, 0: 1}


def test_pop_on_empty(new_pqueue):
    """Test pop with empty priority queue."""
    with pytest.raises(IndexError):
        new_pqueue.pop()


def test_pop_filled(filled_pqueue):
    """Test pop with filled priority queue."""
    assert filled_pqueue.pop() == 4


def test_pop_filled_twice(filled_pqueue):
    """Test popping two times in filled priority queue."""
    filled_pqueue.pop()
    assert filled_pqueue.pop() == 3


def test_pop_filled_to_empty(filled_pqueue):
    """Test popping until priority queue empty."""
    filled_pqueue.pop()
    filled_pqueue.pop()
    filled_pqueue.pop()
    filled_pqueue.pop()
    with pytest.raises(IndexError):
        filled_pqueue.pop()


def test_insert_then_pop_on_empty(new_pqueue):
    """Test insert and then pop on empty priority queue."""
    new_pqueue.insert(1)
    assert new_pqueue.pop() == 1


def test_peek_empty(new_pqueue):
    """Test peek on empty priority queue."""
    with pytest.raises(IndexError):
        new_pqueue.peek()


def test_peek_filled(filled_pqueue):
    """Test peek on filled priority queue."""
    assert filled_pqueue.peek() == 4


def test_peek_filled_insert(filled_pqueue):
    """Test peek on insert high priority in filled priority queue."""
    filled_pqueue.insert(10, -5)
    assert filled_pqueue.peek() == 10


def test_peek_filled_insert_low_priority(filled_pqueue):
    """Test peek on insert low priority in filled priority queue."""
    filled_pqueue.insert(10, -0.5)
    assert filled_pqueue.peek() == 4


def test_pop_then_insert_filled(filled_pqueue):
    """Test pop then insert by peeking."""
    filled_pqueue.pop()
    filled_pqueue.insert(10, -5)
    assert filled_pqueue.peek() == 10
