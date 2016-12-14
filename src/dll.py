"""An implementation of a doubly linked list in Python."""


class Node():
    """Instantiate a node."""

    def __init__(self, value=None, nxt=None, previous=None):
        """."""
        self.value = value
        self.next = nxt
        self.previous = previous


class DbLinkedList():
    """Instantiate a doubly linked list."""

    def __init__(self, value=None):
        """."""
        self.head = None
        self.tail = None
        if value:
            self.push(value)

    def push(self, value=None):
        """Push value to the head of dll."""
        new_node = Node(value, self.head, None)
        orig_node = self.head
        self.head = new_node
        new_node.next = orig_node
        if self.tail is None:
            self.tail = self.head

    def append(self, value):
        """Append value to the tail of dll."""
        new_node = Node(value, None, self.tail)
        orig_node = self.tail
        self.tail = new_node
        new_node.prev_node = orig_node
        if self.head is None:
            self.head = self.tail

    def pop(self):
        """Pop first value off of the head of dll."""
        if self.head:
            returned_value = self.head.value
            self.head = self.head.next
            return returned_value
        raise ValueError("Cannot pop from an empty list")
