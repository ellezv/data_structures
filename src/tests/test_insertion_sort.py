"""Test file for insertion sort."""


import math


def test_simple_list():
    """Test sort on a small, simple list."""
    from insertion_sort import insertion_sort
    arr = [1, 2, 3, 4]
    sort = insertion_sort(arr)
    assert sort == [4, 3, 2, 1]


def test_far_more_complex_list():
    """Test sort on a much larger, much more complex list."""
    from insertion_sort import insertion_sort
    large_list = [i for i in range(5000)]
    test_list = []
    for i in large_list:
        test_list.insert(math.floor(i % 7), i)
    sort = insertion_sort(test_list)
    assert sort == large_list[::-1]
