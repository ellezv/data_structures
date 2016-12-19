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


def test_append_one_value(init_deque):
	"""Check the appended value is added to the end of the deque."""
	init_deque.append(0)
	assert init_deque._dblinkedlist.tail.value == 0


def test_length_append_one_value(init_deque):
	"""Check deque length after a value is appended to the end deque."""
	init_deque.append(0)
	assert init_deque._dblinkedlist.length == 6


def test_appendleft_one_value(init_deque):
	"""Check the appended value is added to the front of the deque."""
	init_deque.appendleft(6)
	assert init_deque._dblinkedlist.head.value == 6


def test_length_appendleft_one_value(init_deque):
	"""Check deque length after a value is appended to the front deque."""
	init_deque.appendleft(6)
	assert init_deque._dblinkedlist.length == 6


def test_end_pop_one_value(init_deque):
	""""""
	init_deque.pop()
	assert init_deque._dblinkedlist.tail.value == 2


def test_length_pop_one_value(init_deque):
	""""""
	init_deque.pop()
	assert init_deque._dblinkedlist.length == 4


def test_value_pop_one_value(init_deque):
	""""""
	assert init_deque.pop() == 1
