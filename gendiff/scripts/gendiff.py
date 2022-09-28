#!/usr/bin/env python

# Import third-party modules

# Import build-in modules
import argparse
import json

# Import local modules


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

    # args = parser.parse_args()
    # functions.generate_diff(args.first_file, args.second_file)


def read_and_parse(path_to_file):
    with open(path_to_file, 'r') as file:
        return json.load(file)


def open_two_files(path_to_file1, path_to_file2):
    dict1 = read_and_parse(path_to_file1)
    dict2 = read_and_parse(path_to_file2)
    return dict1, dict2


def compare_files(two_dictionaries_in_tuple):
    dict1, dict2 = two_dictionaries_in_tuple
    set1, set2 = set(dict1), set(dict2)

    # differences = []
    for key in sorted(set1 | set2):
        if dict1[key] == dict2[key]:
            pass


if __name__ == '__main__':
    main()
