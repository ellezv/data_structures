"""An implementation of a doubly linked list in Python."""


class Node():
    """Instantiate a node."""

    def __init__(self, value=None, nxt=None, previous=None):
        self.value = value
        self.next = nxt
        self.previous = previous


class DbLinkedList():
    """Instantiate a doubly linked list."""

    def __init__(self, value=None):
        self.head = None
        self.tail = None
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node.next

    def push(self, value=None):
        """Pushes vale to the head of dll."""
        new_node = Node(val, self.head, None)
        self.head = new_node
        node.next_node = self.orig_node
        node.prev_node = None

