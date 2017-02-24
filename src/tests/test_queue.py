"""Test for our queue module."""
import pytest
from queue import Queue


@pytest.fixture
def new_queue():
    """Initialize new queue."""
    from queue import Queue
    queue = Queue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    return queue


def test_peek():
    """Test queue peek."""
    q = Queue()
    q.enqueue(5)
    peek = q.peek()
    assert(peek == 5)


def test_queue_dequeue():
    """Test queue dequeue."""
    q = Queue()
    q.enqueue(5)
    val = q.dequeue()
    assert(val == 5)


def test_init_queue():
    """Test an initiation of queue."""
    from queue import Queue
    new_queue = Queue()
    assert new_queue.length == 0
    assert new_queue.peek() is None


def test_init_queue_with_value():
    """General test to initiate queue with value."""
    from queue import Queue
    new_queue = Queue(5)
    assert new_queue.peek() == 5
    assert new_queue.length == 1


def test_length_enqueue_in_queue_with_value(new_queue):
    """Test enqueuing in a non-empty queue."""
    new_queue.enqueue(6)
    assert new_queue.length == 4


def test_head_enqueue_in_queue_with_value(new_queue):
    """Test value of head stay the same when enqueuing a queue with value."""
    new_queue.enqueue(6)
    assert new_queue.peek() == 5


def test_dequeue_from_empty_list_raise_err():
    """Test dequeue from an empty list will raise appropriate error."""
    from queue import Queue
    new_queue = Queue()
    msg = "Cannot dequeue from an empty queue"
    with pytest.raises(ValueError, message=msg):
        new_queue.dequeue()


def test_dequeue_sets_new_head(new_queue):
    """Test dequeue from a list with value will set a new head."""
    new_queue.dequeue()
    assert new_queue.peek() == 4


def test_dequeue_return_value(new_queue):
    """Test that return value of removed head."""
    assert new_queue.dequeue() == 5


def test_peek_with_one_value():
    """Test peek from list with one value."""
    from queue import Queue
    new_queue = Queue(1)
    assert new_queue.peek() is 1


def test_peek_on_empty_queue():
    """Test peak from empty queue."""
    from queue import Queue
    empty_queue = Queue()
    assert empty_queue.peek() is None


def test_peek_returns_second_value(new_queue):
    """Test that return value of second in list."""
    assert new_queue.peek() == 5


def test_peek_after_dequeue(new_queue):
    """Test that return value of second in list after dequeued list."""
    new_queue.dequeue()
    assert new_queue.peek() == 4


def test_size_empty_list():
    """Test that return size of empty list."""
    from queue import Queue
    new_queue = Queue()
    assert new_queue.size() == 0


def test_size_with_one_value():
    """Test that return size of list with one value."""
    from queue import Queue
    new_queue = Queue(1)
    assert new_queue.size() == 1


def test_size_with_multi_value(new_queue):
    """Test that return size of list with multiple values."""
    assert new_queue.size() == 3
