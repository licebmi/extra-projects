#!/usr/bin/env python3
import argparse
import random


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate a range of random integers")
    parser.add_argument(
        "-o",
        "--ordered",
        action="store_true",
        dest="ordered",
        help="Returns an ordered range",
    )
    parser.add_argument(
        "-s",
        "--start",
        action="store",
        dest="start",
        type=int,
        default=1,
        help="Specify the start of the range",
    )
    parser.add_argument(
        "ammount",
        action="store",
        type=int,
        default=10,
        nargs="?",
        help="Specify the ammount of digits to return",
    )

    args = parser.parse_args()

    if args.ammount < 0:
        parser.error(f"argument ammount: must be a positive integer: '{args.ammount}'")

    return args


def main():
    args = parse_arguments()
    start = args.start
    end = args.start + args.ammount
    result = []
    number_list = list(range(start, end))
    if not args.ordered:
        random.shuffle(number_list)

    ## Map might be used, as it's generally more efficient, although in this case, a for loop is clearer
    ## and we don't take advantage of many of the more interesting properties of the map function.
    # list(map(print, number_list))

    for n in number_list:
        print(n)


if __name__ == "__main__":
    main()
