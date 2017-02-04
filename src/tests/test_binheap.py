"""Tests for our binheap module."""


import pytest


def test_init_empty():
    """Test binary heap empty on init"""
    from binheap import Binheap
    new_binheap = Binheap()
    assert new_binheap._container == []


def test_init_binheap():
    """Tests initialization of binary heap"""
    from binheap import Binheap
    new_binheap = Binheap([1])
    assert new_binheap._container == [1]


def test_binheap_init_multiple_unordered():
    """Tests init of binary heap"""
    from binheap import Binheap
    new_binheap = Binheap([5, 4, 6, 3, 7, 2, 9])
    assert new_binheap._container == [9, 6, 7, 3, 4, 2, 5]


def test_binheap_init_multiple_unordered_2():
    """Tests init of binary heap"""
    from binheap import Binheap
    new_binheap = Binheap([1, 2, 3, 4])
    assert new_binheap._container == [4, 3, 2, 1]


def test_binheap_push_single_value_container_head():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(1)
    assert new_binheap._container == [1]


def test_binheap_push_two_values_second_greater_than():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(1)
    new_binheap.push(2)
    assert new_binheap._container == [2, 1]


def test_binheap_push_two_values_second_less_than():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(2)
    new_binheap.push(1)
    assert new_binheap._container == [2, 1]


def test_binheap_push_multiple_unordered():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(5)
    new_binheap.push(4)
    new_binheap.push(6)
    new_binheap.push(3)
    new_binheap.push(7)
    new_binheap.push(2)
    new_binheap.push(9)
    assert new_binheap._container == [9, 6, 7, 3, 4, 2, 5]


def test_binheap_push_one_value_pop_one_value():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(2)
    new_binheap.pop()
    assert new_binheap._container == []


def test_binheap_push_two_values_pop_one_value():
    """Tests push on binary heap"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(5)
    new_binheap.push(4)
    new_binheap.pop()
    assert new_binheap._container == [4]


def test_binheap_push_then_pop_multiple():
    """Tests push and pop sequence"""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(1)
    new_binheap.push(2)
    new_binheap.push(3)
    new_binheap.push(4)
    new_binheap.push(5)
    new_binheap.push(6)
    new_binheap.push(7)
    new_binheap.push(8)
    new_binheap.push(9)
    assert new_binheap._container == [9, 8, 6, 7, 3, 2, 5, 1, 4]
    x = new_binheap.pop()
    print(new_binheap._container)
    print(x)
    assert new_binheap._container == [8, 7, 5, 6, 3, 2, 4, 1]
    # new_binheap.push(10)
    # assert new_binheap._container == [10, 8, 5, 7, 3, 2, 4, 1, 6]
    # new_binheap.push(11)
    # assert new_binheap._container == [11, 10, 5, 7, 8, 2, 4, 1, 6, 3]
    # new_binheap.pop()
    # assert new_binheap._container == [10, 8, 4, 7, 5, 2, 3, 1, 6]
    # new_binheap.pop()
    # assert new_binheap._container == [8, 7, 4, 6, 5, 2, 3, 1]
    # new_binheap.pop()
    # new_binheap.pop()
    # new_binheap.pop()
    # new_binheap.pop()
    # new_binheap.pop()
    # new_binheap.pop()
    # new_binheap.pop()
    # assert new_binheap._container == [1]
    # new_binheap.pop()
    # assert new_binheap._container == []