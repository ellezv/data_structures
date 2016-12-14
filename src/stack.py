"""Test for stack module."""


class Node(object):
    """Where all data is stores. Points to next Node."""

    def __init__(self, data=None, next=None):
        """Class constructor to instantiate node with value and next params."""
        self.value = data
        self.next = next


class Stack():
    """Stack that pushes and pops from using existing functions."""

    def __init__(self, iterable=None):
        """Instantiate class with iterable as opitional param."""
        self.head = None
        self.size = 0
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def push(self, val):
        """Push a new node as the head of the linked list."""
        if self.head is None:
            new_node = Node(val, None)
            self.head = new_node
        else:
            new_node = Node(val, self.head)
            self.head = new_node

    def pop(self):
        """Remove a new node from the head of the linked list."""
        if self.head is not None:
            try:
                pop_head = self.head.value
                self.head = self.head.next
                return pop_head
            except ValueError:
                pop_head = self.head.value
                self.head = None
        else:
            raise IndexError('cannot pop from empty list')
