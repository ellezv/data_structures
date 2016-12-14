"""Tests for our stack module."""
import unittest
from stack import Stack


class StackTestCases(unittest.TestCase):
    """class for test cases using unittest."""

    def test_push_pop(self):
        """Basic Test to test the push/pop with one value."""
        from stack import Stack
        lst = Stack()
        lst.push(2)
        val = lst.pop()
        assert val == 2

    def test_push_pop_iter(self):
        """Test for when it tries to pop from empty stack with iterable."""
        from stack import Stack
        lst = Stack([1, 2, 3, 4, 5])
        val = lst.pop()
        assert val == 5
        val = lst.pop()
        assert val == 4
        val = lst.pop()
        assert val == 3
        val = lst.pop()
        assert val == 2
        val = lst.pop()
        assert val == 1

    def test_push_pop_error(self):
        """Test for when it tries to pop from empty stack."""
        lst = Stack()
        with self.assertRaises(IndexError):
            lst.pop()
