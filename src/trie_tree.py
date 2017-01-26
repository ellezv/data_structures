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

    def traversal(self, string, dict_cur=None):
        """Depth first traversal."""
        if dict_cur is None:
            dict_cur = self._root
        if type(string) is str:
            for letter in string:
                try:
                    dict_cur = dict_cur[letter]
                except KeyError:
                    break
            for letter in dict_cur.keys():
                yield letter
                string = string + letter
                dict_cur = dict_cur[letter]
                self.traversal(string, dict_cur)
