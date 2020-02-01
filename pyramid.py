#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from fibonacci import check_input_type


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    """
    rows  width    stones   air
    1       1       1       subtract and divide
    2       3       3
    3       5       5
    4       7       7
    n       2n-1    2n-1

    1 --=--
    2 -===-
    3 =====

    :param rows:
    :return:
    """
    rows = check_input_type(rows)
    if rows <= 0:
        raise ValueError("The input must be a non-negative integer")

    width = 2*rows-1

    for n in range(1, rows +1):
        stones = 2*n-1
        air = (width - stones) // 2
        print("-"*air + "="*stones + "-"*air)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
    print('test again')
