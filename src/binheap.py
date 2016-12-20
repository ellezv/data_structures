"""Implementation of a binary heap in Python."""
import math


class Binheap(object):
    """."""

    def __init__(self, value=None):
        """Initialize binary heap."""
        self._container = []
        if value:
            self.push(value)

    def push(self, value):
        """Push a value in our heapified list."""
        self._container.append(value)

        a = len(self._container) - 1
        b = math.floor((len(self._container) - 1) / 2)
        while self._container[a] > self._container[b]:
            try:
                self._container[a], self._container[b] = self._container[b], self._container[a]
                a, b = b, math.floor(b / 2)
            except IndexError:
                break
