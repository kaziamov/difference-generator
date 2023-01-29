#!/usr/bin/env python

from gendiff.cli import get_args
from gendiff.diff_generation import generate_diff


def main():
    """Create and print diff from arguments"""
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
