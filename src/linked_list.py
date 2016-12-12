"""Python implementation of a linked list."""


class Node():
    """Instantiate a Node."""

    def __init__(self, value, next_):
        """Instantiate a node with value and next params."""
        self.value = value
        self.next = next_


class LinkedList():
    """Instantiate a Linked List."""

    def __init__(self):
        """Instantiate an empty Linked list."""
        self.head = None
        self.tail = None

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
