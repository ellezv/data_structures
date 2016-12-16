"""Test for our queue module."""

import pytest

@pytest.fixture
def new_queue():
    """Initialize new queue."""
    from queue import Queue
    queue = Queue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    return queue

def test_init_queue():
    """Test a initiation of queue."""
    from queue import Queue
    new_queue = Queue()
    assert new_queue.length == 0
    assert new_queue.head == None
    assert new_queue.tail == None

def test_queue_with_value():
    """General test to initiate queue with value."""
    from queue import Queue
    new_queue = Queue(5)
    assert new_queue.head.value == 5
    assert new_queue.tail.value == 5
    assert new_queue.length == 1

