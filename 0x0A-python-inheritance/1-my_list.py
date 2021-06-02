#!/usr/bin/python3
"""
Class MyList hat inherits from list
"""


class MyList(list):
    """
    class that inherits a list
    """
    def print_sorted(self):
        """Prints self in sorted format
        """
        print(sorted(self))
