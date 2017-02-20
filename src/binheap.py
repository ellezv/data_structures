"""Implementation of a binary heap in Python."""


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
        if value and hasattr(value, "__iter__"):
            for item in value:
                self.push(item)
        elif value:
            raise TypeError('Initial value must be an iterable!')

    def push(self, value):
        """Push a value in our heapified list."""
        self._container.append(value)
        if len(self._container) > 1:
            self.organize_binheap_push()

    def pop(self):
        """Pop a value from the top of the heap."""
        try:
            self._container[0], self._container[len(self._container) - 1] = self._container[len(self._container) - 1], self._container[0]
            val = self._container.pop()
            if len(self._container) > 1:
                self.organize_binheap_pop()
            return val
        except:
            raise IndexError('Cannot pop from an empty binary heap!')

    def organize_binheap_push(self):
        """Organize the binary heap according to the heaps rules.

        This function is optimized for push ie only compare the newly pushed
        value to parents and organize accordingly.

        Max heap: Parent nodes must be greater than child nodes.

        Notes:  Last index number is (container length -1).
                Initial parent index is (container length - 2) / 2 floored.
        """
        a = -1
        b = int((len(self._container) - 2) / 2.)
        while self._container[a] > self._container[b]:
            self._container[a], self._container[b] = self._container[b], self._container[a]
            a, b = b, int((b - 1) / 2.)
            if self._container[a] is self._container[0]:
                break

    def organize_binheap_pop(self):
        """Organize the binary heap according to the heaps rules.

        This function is optimized for pop ie compare all values in the
        heap to parents and organize accordingly.

        Max heap: Parent nodes must be greater than child nodes.
        """
        cond = 1
        while cond == 1:
            for i in range(1, len(self._container) + 1):
                ind = len(self._container) - i
                par = int((ind - 1) / 2.)
                if ind == 0:
                    cond = 0
                    print(cond)
                if self._container[ind] > self._container[par]:
                    self._container[ind], self._container[par] = self._container[par], self._container[ind]
                    break
