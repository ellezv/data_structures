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
    assert deque._dbLinkedList.head is None
    assert deque._dbLinkedList.tail is None
    assert deque._dbLinkedList.length is None


def test_init_deque_with_iter_sets_head(new_deque):
    """Check head value is value expected."""
    assert new_deque._dbLinkedList.head == 5


def test_init_deque_with_iter_sets_tail(new_deque):
    """Check tail value is value expected."""
    assert new_deque._dbLinkedList.tail == 1


def test_init_deque_with_iter_sets_length(new_deque):
    """Check length is increased properly."""
    assert new_deque._dbLinkedList.length == 5
