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
        self.length = 0
        if value:
            self.push(value)

    def push(self, value=None):
        """Push value to the head of dll."""
        new_node = Node(value, nxt=self.head)
        if self.length < 1:
            self.tail = new_node
        else:
            self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def append(self, value):
        """Append value to the tail of dll."""
        new_node = Node(value, None, self.tail)
        if self.length < 1:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        """Pop first value off of the head of dll."""
        if self.head:
            returned_value = self.head.value
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return returned_value
        raise ValueError("Cannot pop from an empty list")

    def shift(self):
        """Remove and return the last value of the dll."""
        if self.head:
            returned_value = self.tail.value
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return returned_value
        raise ValueError("Cannot shift from an empty list")

    def remove(self, value):
        """Remove the value from the dll."""
        curr_node = self.head
        if not self.length:
            raise ValueError("Cannot remove from an empty list")
        else:
            if curr_node.value == value:
                self.pop()
            else:
                while curr_node is not None:
                    if curr_node.value == value:
                        curr_node.previous.next = curr_node.next
                        curr_node.next.previous = curr_node.previous
                        print("{} was removed".format(value))
                        return
                    else:
                        curr_node = curr_node.next
            raise ValueError("{} not in the list".format(value))
