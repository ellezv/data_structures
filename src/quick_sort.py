""""Implementation of a quick-sort algorithm."""


def quick_sort(iterable):
    """Return a sorted list."""
    if len(iterable) < 2:
        return iterable
    pivot = iterable[-1]
    front_half = [number for number in iterable[:-1] if number <= pivot]
    back_half = [number for number in iterable[:-1] if number > pivot]
    if len(front_half) > 1:
        front_half = quick_sort(front_half)
    if len(back_half) > 1:
        back_half = quick_sort(back_half)
    if back_half:
        return front_half + [pivot] + back_half
    if front_half:
        return front_half + [pivot] + back_half
