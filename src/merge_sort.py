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


if __name__ == "__main__":
    import timeit

    easy_sort_time = timeit.repeat(stmt="merge_sort([2,3,1])", setup="from merge_sort import merge_sort", number=500, repeat=1)
    complex_sort_time = timeit.repeat(stmt="merge_sort([i for i in range(1000)][::-1])", setup="from merge_sort import merge_sort", number=500, repeat=1)
    output = """merge sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.

    Input: [2,3,1]
    number of runs: 500
    average time: {0} seconds

    Input: [i for i in range(1000)]
    number of runs: 500
    average time: {1} seconds""".format(easy_sort_time, complex_sort_time)

    print(output)