"""Tests for our stack module."""

import pytest


@pytest.fixture
def new_stack():
    from stack import Stack
    stck = Stack()
    return stck


def test_new_stack_is_empty(new_stack):
    """Test that instantiation of stack is empty."""
    assert new_stack._linkedlist.head is None


def test_push_stack(new_stack):
    """Test that push stack pushes value on top of stack."""
    new_stack.push(5)
    assert new_stack._linkedlist.head.value is 5


def test_pop_stack(new_stack):
    """Test that pop method pops value off top of stack."""
    new_stack.push(5)
    new_stack.pop()
    assert new_stack._linkedlist.head is None


def test_pop_stack_returns_popped_val():
    """Test that pop method returns value popped off."""
    from stack import Stack
    stk = Stack([1, 2, 3, 4, 5])
    assert stk.pop() == 5


def test_new_stack_head_is_last_iter():
    """Test that the new_stack head is the last iterable."""
    from stack import Stack
    stck = Stack([1, 2, 3, 4, 5])
    assert stck._linkedlist.head.value is 5


def test_new_stack_without_iter_raises_typeerr():
    """Test that instantiating a new stack with a non iter raise Type Error."""
    from stack import Stack
    with pytest.raises(TypeError):
        Stack(42)
