"""Implementation of a Trie tree."""


class TrieTree(object):
    """."""

    def __init__(self):
        """Instantiate a Trie tree."""
        self._root = {}
        self._size = 0

    def insert(self, iter):
        """Insert a string in the trie tree."""
        if type(iter) is str:
            if not self.contains(iter):
                self._size += 1
                start = self._root
                for letter in iter:
                    start.setdefault(letter, {})
                    start = start[letter]
                start["$"] = {}
            return
        raise TypeError("Please enter a string.")

    def contains(self, value):
        """Will return True if the string is in the trie, False if not."""
        if type(value) is str:
            start = self._root
            for letter in value:
                try:
                    start = start[letter]
                except KeyError:
                    return False
            if "$" in start.keys():
                return True
        return False

    def size(self):
        """Return the size of the Trie tree. O if empty."""
        return self._size

    def remove(self, value):
        """Will remove the given string from the trie."""
        if type(value) is str:
            current_letter = self._root
            nested = []
            for letter in value:
                try:
                    current_letter = current_letter[letter]
                    nested.insert(0, current_letter)

                except KeyError:
                    raise KeyError("Cannot remove a word that is not in the Trie.")
            if "$" in current_letter.keys():
                del(current_letter['$'])
                if len(current_letter.keys()):
                    self._size -= 1
                    return
            else:
                raise KeyError("Cannot remove a word that is not in the Trie.")
            nested.pop(0)
            for idx, letter in enumerate(value[::-1]):
                if len(nested[idx].keys()) > 1:
                    self._delete_word(nested[idx][letter], value)
                    break
                else:
                    self._delete_word(nested[idx][letter], value)
            self._size -= 1
            return

    def _delete_word(self, nested_dict, value):
            """Helper function to delete nested dictionary."""
            current_letter = self._root
            for letter in value:
                if current_letter[letter] == nested_dict:
                    del current_letter[letter]
                    return
                current_letter = current_letter[letter]
