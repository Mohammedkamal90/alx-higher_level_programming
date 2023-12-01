#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)

def find_peak_recursive(lst, low, high):
    """Helper function for recursive binary search."""
    if low == high:
        return lst[low]

    mid = (low + high) // 2

    if lst[mid] > lst[mid + 1]:
        return find_peak_recursive(lst, low, mid)
    else:
        return find_peak_recursive(lst, mid + 1, high)

