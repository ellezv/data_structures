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
            self.head.previous = None
            return returned_value
        raise ValueError("Cannot pop from an empty list")

    def shift(self):
        """Remove last value off of the tail of dll."""
        if self.tail:
            returned_value = self.tail.value
            self.tail = self.tail.previous
            self.tail.next = None
            return returned_value
        raise ValueError("Cannot shift from an empty list")

    def remove(self, val):
        """Search for node with matching value and remove it."""
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                if self.head == curr_node:
                    self.head = curr_node.next
                    self.head.previous = None
                elif self.tail == curr_node:
                    self.tail = self.tail.previous
                    self.tail = None
                else:
                    curr_node.previous.next = curr_node.next
                    curr_node.next.previous = curr_node.previous
            else:
                curr_node = curr_node.next
        return None
