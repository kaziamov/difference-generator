#!/usr/bin/env python

# Import build-in modules
import argparse


def main():
    """Сreate documentation for programm"""
    parser = argparse.ArgumentParser(prog='gendiff', description='Program for compare two files and print difference.')
    parser.add_argument('first_file',
                        help='First file to compare')
    parser.add_argument('second_file',
                        help='Second file to compare')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='Get choice for output file format')

    args = parser.parse_args()
    # print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
