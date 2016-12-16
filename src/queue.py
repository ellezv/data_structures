"""An implementation of a queue in Python."""

from dll import DbLinkedList


class Queue(object):
    """Create a queue which inherits from Double-linked List."""

    def __init__(self, value=None, next=None, previous=None):
        """Initialize new queue from dll using composition."""
        self._dblinkedlist = DbLinkedList()
        if value:
            self._dblinkedlist.append(value)
        self.head = self._dblinkedlist.head
        self.tail = self._dblinkedlist.tail
        self.length = self._dblinkedlist.length

    def enqueue(self, value):
        """Add value to the tail of the queue."""
        self._dblinkedlist.append(value)
        self.head = self._dblinkedlist.head
        self.tail = self._dblinkedlist.tail
        self.length = self._dblinkedlist.length

    def dequeue(self):
        """Remove the first item in the queue and return value."""
        try:
            dequeued_value = self._dblinkedlist.pop()
            self.head = self._dblinkedlist.head
            self.tail = self._dblinkedlist.tail
            self.length = self._dblinkedlist.length
            return dequeued_value
        except ValueError:
            raise ValueError("Cannot dequeue from an empty queue")

    def peek(self):
        """Return next value in the queue without dequeuing."""
        try:
            return self._dblinkedlist.head.next.value
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue."""
        return self.length
