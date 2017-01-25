"""Implementation of a Trie tree."""

class TrieTree(object):
    """."""

    def __init__(self):
        """Instantiate a Trie tree."""
        self._root = {}
        self._size = 0

    def insert(self, iter):
        """insert a string in the trie tree."""
        if iter and hasattr(iter, str):
            if not self.contains(iter):
                self._size += 1
                start = self._root
                for letter in iter:
                    start.setdefault(letter, {})
                    start = start[letter]
                start["$"] = {}
            return
        raise ValueError("Please enter a string.")

    def contains(self, value):
        """will return True if the string is in the trie, False if not."""
        if value and hasattr(value, str):
            start = self._root
            for letter in value:
                try:
                    start = start[letter]
                except KeyError:
                    return False
            if "$" in start.keys():
                return True
        return False
