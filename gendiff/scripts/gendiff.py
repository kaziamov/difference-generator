#!/usr/bin/env python

# Import build-in modules
import argparse

# Import local modules
from functions import functions


def main():
    """Сreate documentation for program"""
    parser = argparse.ArgumentParser(prog='gendiff', description='Program for compare two files and print difference.')
    parser.add_argument('first_file',
                        help='First file to compare')
    parser.add_argument('second_file',
                        help='Second file to compare')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='Get choice for output file format')

    args = parser.parse_args()
    functions.generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
