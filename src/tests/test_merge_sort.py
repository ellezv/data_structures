"""Test file for merge sort."""


def test_merge_sort():
    """Sort works."""
    from merge_sort import merge_sort
    ms = merge_sort([2, 1, 7, 4, 8, 6, 5, 3])
    assert ms == [1, 2, 3, 4, 5, 6, 7, 8]