"""Implementation of a stack in Python, inheriting from a linked list."""
from linked_list import LinkedList


class Stack(object):
    """Create stack which inherits from LinkedList class."""

    def __init__(self, iterable=None):
        """Create a new stack, from LinkedList using composition."""
        self._linkedlist = LinkedList()
        if iterable and hasattr(iterable, "__iter__"):
            for item in iterable:
                self.push(item)
        elif iterable:
            raise TypeError

    def push(self, value):
        """Push a new value on top of the stack."""
        self._linkedlist.push(value)

    def pop(self):
        """Pop the first value of the stack."""
        return self._linkedlist.pop()
