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
            self.push(value)

    def push(self, value=None):
        """Pushes vale to the head of dll."""
        new_node = Node(value, self.head, None)
        orig_node = self.head
        self.head = new_node
        new_node.next = orig_node
        new_node.prev_node = None
        if self.tail is None:
            self.tail = orig_node

