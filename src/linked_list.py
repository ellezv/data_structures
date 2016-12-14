"""Python implementation of a linked list."""


class Node():
    """Instantiate a Node."""

    def __init__(self, value=None, next=None):
        """Instantiate a node with value and next params."""
        self.value = value
        self.next = next


class LinkedList():
    """Instantiate a Linked List."""

    def __init__(self, iterable=None):
        """Instantiate an empty Linked list."""
        self.head = None

        if iterable and hasattr(iterable, "__iter__"):
            for item in iterable:
                self.push(item)
        elif iterable:
            raise TypeError

    def push(self, val):
        """Push a new node as the head of the linked list."""
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        """Pop first value off linked list and return value."""
        # if self.head is None:
        if self.head is not None:
            pop_head = self.head.value
            self.head = self.head.next
            return pop_head
        else:
            raise IndexError('cannot pop from empty list')

    def search(self, val):
        """Search for the value in a list of nodes."""
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                return curr_node
            else:
                curr_node = curr_node.next
        return None

    def remove(self, val):
        """Search for node with matching value and removes it."""
        if self.head.value == val:
            self.head = self.head.next
            return
        curr_node = self.head.next
        prev_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                prev_node.next = curr_node.next
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def size(self):
        """Return the length of the linked list."""
        if self.head is not None:
            size = 1
            curr = self.head
            while curr.next is not None:
                size += 1
                curr = curr.next
            return size
        return 0

    def display(self):
        """Return the linked list as a printed string of a tuple literal."""
        output = "("
        current = self.head
        while current is not None:
            if type(current.value) == str:
                output += "'" + current.value + "'"
            else:
                output += str(current.value)
            if current.next is not None:
                output += ', '
            current = current.next
        return output + ")"
