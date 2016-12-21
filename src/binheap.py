"""Implementation of a binary heap in Python."""
import math


class Binheap(object):
    """A binary heap (max heap).

    The binary heap pushes the largest values up
    to the top of the heap. Values must be numbers.

    push(val) Pushes a value into the binary heap.
    pop() Pops a value off the top of the binary heap.
    """

    def __init__(self, value=None):
        """Initialize binary heap."""
        self._container = []
        if value:
            self.push(value)

    def push(self, value):
        """Push a value in our heapified list."""
        self._container.append(value)
        if len(self._container) > 1:
            self.organize_binheap()

    def pop(self):
        """Pop a value from the top of the heap."""
        try:
            self._container[0], self._container[len(self._container) - 1] = self._container[len(self._container) - 1], self._container[0]
            self._container.pop()
            if len(self._container) > 1:
                self.organize_binheap()
        except:
            raise IndexError('Cannot pop from an empty binary heap!')

    def organize_binheap(self):
        """Organize the binary heap according to the heaps rules.

        Max heap: Parent nodes must be greater than child nodes.

        Notes:  Last index number is (container length -1).
                Parent index is (container length - 2) / 2 floored.
        """
        a = len(self._container) - 1
        b = int(math.floor((len(self._container) - 2) / 2))
        while self._container[a] > self._container[b]:
            self._container[a], self._container[b] = self._container[b], self._container[a]
            a, b = b, int(math.floor((b - 1) / 2))
            if self._container[a] is self._container[0]:
                break
