"""Tests for our binheap module."""


import pytest

PARAMS_MULTIPLE_UNORDERED = [
    ([5, 4, 6, 3, 7, 2, 9], [9, 6, 7, 3, 4, 2, 5]),
    ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 6, 7, 3, 2, 5, 1, 4]),
    ([1, 4, 2, 6, 7, 3, 4, 7, 1, 5345, 23, 6, 53], [5345, 23, 53, 7, 7, 6, 3, 1, 1, 4, 6, 2, 4]),
    ([], []),
    ([1], [1]),
]


def test_init_empty():
    """Test binary heap empty on init."""
    from binheap import Binheap
    new_binheap = Binheap()
    assert new_binheap._container == []


def test_init_binheap():
    """Test initialization of binary heap."""
    from binheap import Binheap
    new_binheap = Binheap([1])
    assert new_binheap._container == [1]


@pytest.mark.parametrize('n, result', PARAMS_MULTIPLE_UNORDERED)
def test_binheap_init_multiple_unordered(n, result):
    """Test init of binary heap."""
    from binheap import Binheap
    new_binheap = Binheap(n)
    assert new_binheap._container == result


def test_binheap_init_multiple_unordered_2():
    """Test init of binary heap."""
    from binheap import Binheap
    new_binheap = Binheap([1, 2, 3, 4])
    assert new_binheap._container == [4, 3, 2, 1]


def test_binheap_push_single_value_container_head():
    """Test push on binary heap."""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(1)
    assert new_binheap._container == [1]


def test_binheap_push_two_values_second_greater_than():
    """Test push on binary heap."""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(1)
    new_binheap.push(2)
    assert new_binheap._container == [2, 1]


def test_binheap_push_two_values_second_less_than():
    """Test push on binary heap."""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(2)
    new_binheap.push(1)
    assert new_binheap._container == [2, 1]


def test_binheap_push_multiple_unordered():
    """Test push on binary heap."""
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
    """Test push on binary heap."""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(2)
    new_binheap.pop()
    assert new_binheap._container == []


def test_binheap_push_two_values_pop_one_value():
    """Test push on binary heap."""
    from binheap import Binheap
    new_binheap = Binheap()
    new_binheap.push(5)
    new_binheap.push(4)
    new_binheap.pop()
    assert new_binheap._container == [4]


def test_binheap_push_then_pop_multiple():
    """Test push and pop sequence."""
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
    assert new_binheap.pop() == 9
