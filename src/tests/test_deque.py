"""Tests for our deque module."""

import pytest

@pytest.fixture
def init_deque():
    """Init a new deque and returns it."""
    from deque import Deque
    new_deque = Deque([1,2,3,4,5])
    return new_deque


def test_init_deque_no_param_is_empty():
    """Test new deque is empty."""
    from deque import Deque
    deque = Deque()
    assert deque._dblinkedlist.head is None
    assert deque._dblinkedlist.tail is None
    assert deque._dblinkedlist.length == 0


def test_init_deque_with_iter_sets_head(init_deque):
    """Check head value is value expected."""
    assert init_deque._dblinkedlist.head.value == 1


def test_init_deque_with_iter_sets_tail(init_deque):
    """Check tail value is value expected."""
    assert init_deque._dblinkedlist.tail.value == 5


def test_init_deque_with_iter_sets_length(init_deque):
    """Check length is increased properly."""
    assert init_deque._dblinkedlist.length == 5
