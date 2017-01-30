"""Insertion sort algorithm."""


def insertion_sort(input_list):
    """Inertion algorithm."""
    for i in range(len(input_list)):
            while input_list[i] > input_list[i - 1] and i is not 0:
                item = input_list.pop(i)
                input_list.insert(i - 1, item)
                i -= 1
    return input_list


if __name__ == "__main__":
    import timeit

    easy_sort_time = timeit.repeat(stmt="insertion_sort([2,3,1])", setup="from insertion_sort import insertion_sort", number=500, repeat=1)
    complex_sort_time = timeit.repeat(stmt="insertion_sort([i for i in range(100)])", setup="from insertion_sort import insertion_sort", number=500, repeat=1)
    output = """Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.

    Input: [2,3,1]
    number of runs: 500
    average time: {0} seconds

    Input: [i for i in range(100)]
    number of runs: 500
    average time: {1} seconds""".format(easy_sort_time, complex_sort_time)

    print(output)
