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
                self._values.setdefault(value, self._root_node)
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

    def delete(self, value):
        """Delete a nose from the tree."""
        try:
            node = self._values[value]
        except KeyError:
            raise ValueError("You can't delete an nonexistant node.")
        parent = self._find_parent(node)
        if parent is None:
            if node.left is None and node.right is None:
                self._root_node = None
            else:
                new_node = node.left
                while new_node.right is not None:
                    new_node = new_node.right
                self.delete(new_node.value)
                self._size += 1  # to counter the decrement during recursion
                new_node.left, new_node.right = node.left, node.right
                self._root_node = new_node
        else:
            if node.left is None and node.right is None:
                self._delete_node_with_no_children(value, parent)
            elif node.left is not None and node.right is not None:
                self._delete_node_with_two_children(node, parent)
            else:
                self._delete_node_with_one_child(node, parent, value)
        del self._values[node.value]
        self._size -= 1

    def _improper_delete(self, value):
        """A delete function I made for fun that I can imagine would be frowned upon."""
        values = []
        gen = self.breadth_first()
        for i in range(len(self._values)):
            values.append(next(gen))
        values.remove(value)
        self._values = {}
        self._root_node = None
        self._left_depth = 0
        self._right_depth = 0
        self._size = 0
        for v in values:
            self.insert(v)

    def _find_parent(self, node):
        """A helper function to find the parent of a given node."""
        for key in self._values.keys():
            if self._values[key].left is node or self._values[key].right is node:
                return self._values[key]
        return None

    def _delete_node_with_no_children(self, value, parent):
        """Helper function to delete a node with no children."""
        if value < parent.value:
            parent.left = None
        else:
            parent.right = None

    def _delete_node_with_two_children(self, node, parent):
        """A helper function to delte a node with two children."""
        new_node = node.left
        while new_node.right is not None:
            new_node = new_node.right
        new_node_parent = self._find_parent(new_node)
        new_node_parent.right = new_node.left
        if node.left is new_node:
            new_node.right = node.right
        elif node.right is new_node:
            new_node.left = node.left
        else:
            new_node.left, new_node.right = node.left, node.right
        if new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def _delete_node_with_one_child(self, node, parent, value):
        """A helper function to delete a node with one child."""
        if node.left is None:
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left

    def _balance_self(self):
        """Balance the tree is needed."""
        # leaning to the left
        if self.balance < -1:

        # leaning to the right
        elif self.balance > 1:
            pivot_node = self._find_pivot()

    def _find_pivot(self):
        """Helper function that finds the pivot node of an off balanced tree."""
        nodes = sorted(self._values.keys())
        return nodes[int(len(nodes) / 2)]


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


if __name__ == '__main__':  # pragma: no cover
    bst = BinarySearchTree()
    a = [2, 1, 3, 4, 5, 6]
    for i in a:
        bst.insert(i)
