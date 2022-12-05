#!/usr/bin/env python

# Import third-party modules

# Import build-in modules
import argparse
import json
from re import L

# Import local modules
from gendiff.scripts.parsing import read_and_parse
from gendiff.scripts.formatting import format_diff


def main():
    """Сreate command-line interface for program"""
    parser = argparse.ArgumentParser(prog='gendiff', description='Program for compare two files and print difference.')
    parser.add_argument('first_file',
                        help='First file to compare')
    parser.add_argument('second_file',
                        help='Second file to compare')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='Get choice for output file format')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(path_to_file1, path_to_file2):
    """Generate tree of difference from two dictionaries."""
    gendiff = {'status': 'root',
               'child': compare_files(read_and_parse(path_to_file1), read_and_parse(path_to_file2))
    }
    result = format_diff(gendiff)
    return result


def open_two_files(path_to_file1, path_to_file2):
    """Open two files and return it like dictionaries."""
    dict1 = read_and_parse(path_to_file1)
    dict2 = read_and_parse(path_to_file2)
    return dict1, dict2


def compare_files(dict1, dict2):
    """Make compare between two dictionaries."""
    all_keys = sorted((dict1 | dict2).keys())
    types = [list, dict, tuple, set, frozenset]
    differences = []
    for index, key in enumerate(all_keys):
        if key not in dict2:
            d = {'id': index,
                 'status': 'first_only',
                 'key': key,
                 'value1': dict1[key]
                 }
        elif key not in dict1:
            d = {'id': index,
                 'status': 'second_only',
                 'key': key,
                 'value2': dict2[key]
                 }
        elif dict1[key] == dict2[key]:

            d = {'id': index,
                 'status': 'same',
                 'key': key,
                 'value': dict1[key]
                 }
        elif type(dict1[key]) == dict and type(dict2[key]) == dict:
            d = {'id': index,
                    'status': 'child',
                    'key': key,
                    'child': compare_files(dict1[key], dict2[key])
                    }
        else:
            d = {'id': index,
                    'status': 'not_same',
                    'key': key,
                    'value1': dict1[key],
                    'value2': dict2[key]
                    }
        differences.append(d)

    return differences


# if __name__ == '__main__':
#     main()
