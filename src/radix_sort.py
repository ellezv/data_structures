"""Radix sort."""


def radix_sort(iterable):
    """A radix sort method."""
    flat_list = []
    buckets = [[] for i in range(10)]
    longest_num = 0
    for num in iterable:
        if len(str(num)) > longest_num:
            longest_num = len(str(num))
        buckets[int(str(num)[-1])].append(num)
    for i in range(longest_num):
        flat_list = [num for bucket in buckets for num in bucket]
        buckets = [[] for i in range(10)]
        for num in flat_list:
            try:
                index = int(str(num)[-i + 1])
            except IndexError:
                index = 0
            buckets[index].append(num)
    return [num for bucket in buckets for num in bucket]