"""Implementation of a binary search tree."""


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self):
        """Init bst."""
        self._values = {}
        self._root_node = None
        self._left_depth = 0
        self._right_depth = 0
        self._size = 0

    def insert(self, value):
        """Insert a values, ignores if value is already in bst."""
        try:
            if self._values[value]:
                return value
        except KeyError:
            if self._root_node is None:
                self._root_node = Node(value)
                self._values.setdefault(value, Node(value))
                self._size += 1
                return
            node = self._root_node
            depth = 1
            self._size += 1
            while True:
                if value > node.value:
                    if node.right is None:
                        node.right = Node(value, depth)
                        self._values.setdefault(value, node.right)
                        self._side_depth(value, depth)
                        return
                    node = node.right
                    depth += 1
                elif value < node.value:
                    if node.left is None:
                        node.left = Node(value, depth)
                        self._values.setdefault(value, node.left)
                        self._side_depth(value, depth)
                        return
                    node = node.left
                    depth += 1

    def _side_depth(self, value, depth):
        """Helper function to find what side depth to increment."""
        if value > self._root_node.value:
            side = "right"
        else:
            side = "left"
        if side == "left" and depth > self._left_depth:
            self._left_depth = depth
        elif side == "right" and depth > self._right_depth:
            self._right_depth = depth

    def search(self, value):
        """Return the node containing that value or None if not in Tree."""
        try:
            return self._values[value]
        except KeyError:
            return None

    def size(self):
        """Return the number of nodes in the bst."""
        return self._size

    def depth(self):
        """Return the depth of BST."""
        if self._root_node is None:
            raise AttributeError('The tree is empty, it has no depth.')
        if self._left_depth > self._right_depth:
            return self._left_depth
        return self._right_depth

    def contains(self, value):
        """Return True if value is in the bst alse return False."""
        try:
            if self._values[value]:
                return True
        except KeyError:
            return False

    def balance(self):
        """Return positive or negative integer based on what side the tree leans towards."""
        return self._right_depth - self._left_depth

    def breadth_first(self, parent=None, path=None):
        """A breadth first traversal of our tree."""
        if path is None:
            path = [self._root_node.value]
        if parent is None:
            parent = [self._root_node]
        children = []
        while True:
            for node in parent:
                children.append(node.left)
                children.append(node.right)
                path.extend([node.value for node in children])
            parent = children
            yield path



class Node(object):
    """Node."""

    def __init__(self, val, depth=0):
        """Init node."""
        self.value = val
        self.left = None
        self.right = None
        self.depth = depth
