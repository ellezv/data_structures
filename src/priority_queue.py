"""An implementation of a priority queue using a dictionary in Python."""


class PriorityQueue(object):
    """That's it."""

    def __init__(self, tup=None):
        """Initialize a priority queue with default value as None."""
        self._container = {}
        if tup and type(tup) == tuple:
            self.insert(tup)
        elif tup:
            raise TypeError("Must initialize with tuple!")

    def insert(self, tup):
        """Insert tuple in priority queue."""
        pass
