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

    def in_order(self):
        """An in order traversal of our tree."""
        if self._root_node:
            for node in self._root_node.in_order_node():
                yield node

    def pre_order(self):
        """A pre order traversal of our tree."""
        if self._root_node:
            for node in self._root_node.pre_order_node():
                yield node

    def post_order(self):
        """A post order traversal for our tree."""
        if self._root_node:
            for node in self._root_node.post_order_node():
                yield node

    def breadth_first(self):
        """A breadth first traversal of our tree."""
        queue = []
        queue.append(self._root_node)
        while queue:
            node = queue.pop(0)
            yield node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class Node(object):
    """Node."""

    def __init__(self, val, depth=0):
        """Init node."""
        self.value = val
        self.left = None
        self.right = None
        self.depth = depth

    def in_order_node(self):
        """In order traversal for node."""
        if self.left:
            for node in self.left.in_order_node():
                yield node
        yield self.value
        if self.right:
            for node in self.right.in_order_node():
                yield node

    def pre_order_node(self):
        """Pre order traversal for node."""
        yield self.value
        if self.left:
            for node in self.left.pre_order_node():
                yield node
        if self.right:
            for node in self.right.pre_order_node():
                yield node

    def post_order_node(self):
        """Post order traversal for node."""
        if self.left:
            for node in self.left.post_order_node():
                yield node
        if self.right:
            for node in self.right.post_order_node():
                yield node
        yield self.value


if __name__ == '__main__':
    bst = BinarySearchTree()
    a = [20, 9, 22, 7, 12, 21, 25]
    for i in a:
        bst.insert(i)
