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
    # gendiff = 
    return compare_files(read_and_parse(path_to_file1), read_and_parse(path_to_file2))
    # return format_diff(gendiff)
    

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


def is_child(first, second):
    types = [list, dict, tuple, set, frozenset]
    return type(first) in types and type(second) in types


def compare_files(dict1, dict2):
    set1, set2 = set(dict1), set(dict2)
    all_keys = sorted(set1 | set2)
    differences = []
    for index, key in enumerate(all_keys):
        if key in dict1 and key not in dict2:
            d = {'id': index, 'status': 'first_only', 'key': key, 'value': dict1[key]}
        elif key in dict2 and key not in dict1:
            d = {'id': index, 'status': 'second_only', 'key': key, 'value': dict2[key]}
        elif dict1[key] == dict2[key]:
            
            d = {'id': index, 'status': 'same', 'key': key, 'value': dict1[key]}
        else:
            if is_child(dict1[key], dict2[key]):
                d = {'id': index, 'status': 'child', 'key': key, 'value': compare_files(dict1[key], dict2[key])}
            else:
                d = {'id': index, 'status': 'not_same', 'key': key, 'value': dict1[key], 'value2': dict2[key]}
        differences.append(d)
    return differences


if __name__ == '__main__':
    main()
