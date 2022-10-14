#!/usr/bin/env python

# Import third-party modules

# Import build-in modules
import argparse
import json

# Import local modules
from gendiff.scripts.parsing import read_and_parse


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
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(path_to_file1, path_to_file2):
    gendiff = compare_files(open_two_files(path_to_file1, path_to_file2))
    return format_diff(gendiff)
    

def format_diff(data, tabs=2):
    formated_data = '{\n'
    for element in data:
        formated_data += ' ' * tabs
        if type(data[element]) is dict:
            child = format_diff(data[element], tabs=tabs+4)
            formated_data += f'{element}: {child}'
        else:
            formated_data += f'{element}: {json.dumps(data[element])}'
        formated_data += '\n'
    formated_data += ' ' * (tabs - 2) + '}'
    return formated_data.replace('"', '')


def open_two_files(path_to_file1, path_to_file2):
    dict1 = read_and_parse(path_to_file1)
    dict2 = read_and_parse(path_to_file2)
    return dict1, dict2


def compare_files(two_dictionaries_in_tuple):
    dict1, dict2 = two_dictionaries_in_tuple
    set1, set2 = set(dict1), set(dict2)

    differences = {}
    types = [list, dict, tuple, set, frozenset]
    all_keys = sorted(set1 | set2)
    for key in all_keys:
        if key in set1 and key in set2:
            if dict1[key] == dict2[key]:
                if type(dict1[key]) in types:
                    child = compare_files((dict1[key], dict2[key]))
                    differences[f'  {key}'] = child
                else:
                    differences[f'  {key}'] = dict1[key]
            elif type(dict1[key]) in types and type(dict2[key]) in types:
                child = compare_files((dict1[key], dict2[key]))
                differences[f'  {key}'] = child
            else:
                differences[f'- {key}'] = dict1[key]
                differences[f'+ {key}'] = dict2[key]
        elif key in set1:
            differences[f'- {key}'] = dict1[key]
        elif key in set2:
            differences[f'+ {key}'] = dict2[key]
    return differences


if __name__ == '__main__':
    main()
