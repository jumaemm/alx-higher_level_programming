#!/usr/bin/python3
"""prints a sorted list"""


class MyList(list):
    """list subclass"""

    def __init__(self):
        """Initializes a MyList object"""

        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""

        print(sorted(self))
