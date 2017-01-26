"""Implementation of a Trie tree."""


class TrieTree(object):
    """."""

    def __init__(self):
        """Instantiate a Trie tree."""
        self._root = {}
        self._size = 0
        self._cur_dict = self._root

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
            for letter in value:
                try:
                    current_letter = current_letter[letter]
                except KeyError:
                    break
            if "$" in current_letter.keys():
                del(current_letter['$'])
                if len(current_letter.keys()):
                    return
            for letter in value[::-1]:
                current_letter = letter
                if current_letter is {}:
                    del current_letter
                else:
                    break
        raise KeyError("Cannot remove a word that is not in the Trie.")

    def traversal(self, string):
        """Depth first traversal."""
        if type(string) is str:
            current_letter = self._cur_dict
            for letter in string:
                try:
                    current_letter = current_letter[letter]
                except KeyError:
                    break
            self._cur_dict = current_letter
            for letter in self._cur_dict.keys():
                yield letter
                string = string + letter
                self._cur_dict = self._cur_dict[letter]
                self.traversal(string)
