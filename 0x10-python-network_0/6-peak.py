#!/usr/bin/python3


def find_peak(list_of_integers):
    """Find a peak in a list of numbers
    """
    for i in range(0, len(list_of_integers)):
        if ((list_of_integers[i] >= list_of_integers[i - 1]) and
                (list_of_integers[i] >= list_of_integers[i + 1])):
            pick_number = list_of_integers[i]
    return pick_number
