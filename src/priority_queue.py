"""An implementation of a priority queue using a dictionary in Python."""


class PriorityQueue(object):
    """That's it."""

    def __init__(self):
        """Initialize a priority queue with default value as None."""
        self._container = {}

    def insert(self, value, priority=0):
        """Insert tuple in priority queue."""
        if priority > 0:
            raise ValueError('Priorities can only be negative, David.')
        self._container.setdefault(priority, []).append(value)

    def pop(self):
        """"""
        try:
            highest_priority = min([priority for priority in self._container])
            highest_priority_value = self._container[highest_priority].pop(0)
            if not len(self._container[highest_priority]):
                self._container.pop(highest_priority)
            return highest_priority_value
        except ValueError:
            raise IndexError('Cannot pop from an empty priority queue!')

    def peek(self):
        """"""
        try:
            highest_priority = min([priority for priority in self._container])
            return self._container[highest_priority][0]
        except ValueError:
            raise IndexError('There is nothing to see there, David.')