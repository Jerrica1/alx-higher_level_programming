#!/usr/bin/python3
"""
6-peak.py
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    ints = list_of_integers
    length = len(list_of_integers)

    if ints is None or length == 0:
        return None

    num = None

    if ints[0] >= ints[1]:
        return ints[0]
    if ints[length - 1] >= ints[length - 2]:
        return ints[length - 1]

    for i in range(1, length - 1):
        num = ints[i]
        if i < len(ints) - 1:
            if num >= ints[i + 1] and num >= ints[i - 1]:
                break

    return num
