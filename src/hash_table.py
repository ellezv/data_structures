"""Implaementation of a hash table."""


class HashTable(object):
    """A hash table."""

    def __init__(self, size=10):
        """Init the hash table."""
        if type(size) is not int or size < 1:
            raise TypeError('Size must be a positive integer greater than zero.')
        self._size = size
        self._table = [[] for i in range(size)]

    def get(self, key):
        """Return the value paired with the key."""
        bucket = self._hash(key)

    def set(self, key, value):
        """Create a key value pair for the given key and value."""
        if type(key) is not str:
            return 'Key must be a string.'
        self._table[self._hash(key)].append(value)

    def _hash(self, key):
        """Create a hash for the given key."""
        return sum([ord(i) for i in key]) % self._size
