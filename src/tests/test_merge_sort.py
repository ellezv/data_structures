"""Test file for merge sort."""

import random

UNSORTED = [random.randint(0, 100) for i in range(100)]
UNSORTED_ODD = [random.randint(0, 100) for i in range(99)]


def test_merge_sort():
    """Sort works."""
    from merge_sort import merge_sort
    ms = merge_sort([2, 1, 7, 4, 8, 6, 5, 3])
    assert ms == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_sort_random_list():
    """Sorting a long random list of int."""
    from merge_sort import merge_sort
    ms = merge_sort(UNSORTED)
    assert ms == sorted(UNSORTED)


def test_merge_sort_odd_random_list():
    """Sorting a long odd random list of int."""
    from merge_sort import merge_sort
    ms = merge_sort(UNSORTED_ODD)
    assert ms == sorted(UNSORTED_ODD)
