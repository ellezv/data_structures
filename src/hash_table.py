"""Implaementation of a hash table."""


class HashTable(object):
    """A hash table."""

    def __init__(self, size=10, hash_type='additive'):
        """Init the hash table."""
        if type(size) is not int or size < 1:
            raise TypeError('Size must be a positive integer greater than zero.')
        self._size = size
        self._table = [[] for i in range(size)]
        if hash_type is not 'additive' and hash_type is not 'bernstein':
            raise TypeError('The second argument of hash type must be either additive or bernstein.')
        self._hash_type = hash_type

    def get(self, key):
        """Return the value paired with the key."""
        bucket = self._hash(key)
        for pair in self._table[bucket]:
            if pair[0] == key:
                return pair[1]

    def set(self, key, value):
        """Create a key value pair for the given key and value."""
        if type(key) is not str:
            return 'Key must be a string.'
        self._table[self._hash(key)].append((key, value))

    def _hash(self, key):
        """Create a hash for the given key."""
        if self._hash_type is 'additive':
            return self._additive(key)
        return self._bernstein(key)

    def _additive(self, key):
        """An additive hash."""
        return sum([ord(i) for i in key]) % self._size

    def _bernstein(self, key):
        """A bernstein hash."""
        the_hash = 0
        for i in key:
            the_hash = 33 * the_hash + ord(i)
        return the_hash % self._size
