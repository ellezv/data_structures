"""Tests for our deque module."""

def test_init_deque_no_param_is_empty():
    from deque import Deque
    deque = Deque()
    assert deque.head is None
    assert deque.tail is None
    assert deque.length is None


