"""Merge sort."""


import math


def merge_sort(input_list):
    """Merge sort."""
    front_half = input_list[:math.floor(len(input_list) / 2)]
    back_half = input_list[math.floor(len(input_list) / 2):]
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

