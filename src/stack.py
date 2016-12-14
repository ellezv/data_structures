"""Implementation of a stack in Python, inheriting from a linked list."""
from linked_list import LinkedList, Node


class Stack(object):
    """Create stack which inherits from LinkedList class."""

    def __init__(self, head=None, iterable=None):
        """Create a new stack, from LinkedList using composition."""
        self._linkedlist = LinkedList()
        if iterable:
            try:
                for item in iterable:
                    self._linkedlist.head = Node(item)
                    self._linkedlist.length += 1
            except TypeError:
                self._linkedlist.head = iterable
        else:
            self._linkedlist.head = head

    def push(self, value):
        """Push a new value on top of the stack."""
        self._linkedlist.push(value)

    def pop(self):
        """Pop the first value of the stack."""
        self._linkedlist.pop()
