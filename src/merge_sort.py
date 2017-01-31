"""Merge sort."""


import math


def merge_sort(input_list):
    """Merge sort."""
    index = int(math.floor(len(input_list) // 2))
    front_half = input_list[:index]
    back_half = input_list[index:]
    if len(front_half) > 1:
        front_half = merge_sort(front_half)
    if len(back_half) > 1:
        back_half = merge_sort(back_half)
    sorted_list = []
    while front_half and back_half:
        if front_half[0] <= back_half[0]:
            sorted_list.append(front_half.pop(0))
        else:
            sorted_list.append(back_half.pop(0))
    if front_half:
        sorted_list += front_half
    else:
        sorted_list += back_half
    return sorted_list
