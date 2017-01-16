"""Implementation of a binary search tree."""


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self):
        """Init bst."""
        self._values = {}
        self._root_node = None

    def insert(self, value):
        """Insert a values, ignores if value is already in bst."""
        try:
            if self._values[value]:
                return value
        except KeyError:
            if self._root_node is None:
                self._root_node = Node(value)
                self._values.setdefault(value, Node(value))
                return
            node = self._root_node
            while True:
                if value > node.value:
                    if node.right is None:
                        node.right = Node(value)
                        self._values.setdefault(value, node.right)
                        return
                    node = node.right
                elif value < node.value:
                    if node.left is None:
                        node.left = Node(value)
                        self._values.setdefault(value, node.left)
                        return
                    node = node.left

    def search(self, value):
        """Return the node containing that value or None if not in Tree."""
        try:
            return self._values[value]
        except KeyError:
            return None


class Node(object):
    """Node."""

    def __init__(self, val, left=None, right=None):
        """Init node."""
        self.value = val
        self.left = left
        self.right = right
