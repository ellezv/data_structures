"""Insertion sort algorithm."""


def insertion_sort(input_list):
    """Inertion algorithm."""
    for i in range(len(input_list)):
            while input_list[i] > input_list[i - 1] and i is not 0:
                item = input_list.pop(i)
                input_list.insert(i - 1, item)
                i -= 1
    return input_list
