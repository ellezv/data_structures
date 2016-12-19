"""Implementation of a Deque in Python."""

from dll import DbLinkedList


class Deque(object):
    """Implementation of a deque data structure.

    append(value) adds value to the end of the deque.
    appendleft(value) adds value to the front of the deque.
    pop() removes value from the end of the deque.
    popleft() removes a value from the front of the deque.
    peek() returns the tail value without removing it.
    """

    def __init__(self, value=None):
        """Init a deque."""
        self._dblinkedlist = DbLinkedList()
        if value:
            self.append(value)

    def append(self, value):
        """Add value to the end of the deque."""
        self._dblinkedlist.append(value)

    def appendleft(self, value):
        """Add value to the front of the deque."""
        self._dblinkedlist.push(value)

    def pop(self):
        """Remove value from the end of the end of the deque."""
        return self._dblinkedlist.shift()

    def popleft(self):
        """Remove value from the front of the deque."""
        return self._dblinkedlist.pop()

    def peek(self):
        """Return the value of the end of the deque without removing it."""
        if self._dblinkedlist.head is None:
            return self._dblinkedlist
        return self._dblinkedlist.tail.value

    def peekleft(self):
        """Return the value of the front of the deque without removing it."""
        return self._dblinkedlist.head.value

    def size(self):
        """Return the length of the deque."""
        return self._dblinkedlist.length
