#!/usr/bin/env python

# Import third-party modules

# Import build-in modules
import argparse
import json
from re import L

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
    gendiff = compare_files(read_and_parse(path_to_file1), read_and_parse(path_to_file2))
    return format_diff(gendiff)


def format_str(key, value, tabs=4, status=' '):
    tabs_str = [' '] * (tabs - 2)
    tabs_str.extend([status, ' '])
    return '{}{}: {}'.format(''.join(tabs_str), key, value)


def add_brackets(list_):
    result = list_.copy()
    result.insert(0, '{')
    result.insert(-1, '}')
    return result

def format_child(dict_, tabs=4):
    formated_lines = []
    for key, value in dict_.items():
        if type(value) is dict:
            value = format_child(value, tabs + 4)
        formated_lines.append(format_str(key, value, tabs))
    formated_lines.append(' ' * (tabs - 4) + '}')
    return '\n'.join(formated_lines)


def format_diff(data, tabs=0):
    formated_lines = ['{']
    for line in data:
        li = line['value']
        if line['status'] == 'first_only':
            if type(line['value']) is dict:
                li = format_child(li, tabs + 2)
            else:
                li = json.dumps(li)
            formated_lines.append(format_str(line['key'], li, tabs, '-'))

        elif line['status'] == 'second_only':
            if type(line['value']) is dict:
                li = format_child(line['value'], tabs + 2)
            else:
                li = json.dumps(li)
            formated_lines.append(format_str(line['key'], li, tabs, '+'))

        elif line['status'] == 'same':
            if type(line['value']) is dict:
                li = format_child(line['value'], tabs + 4)
            else:
                li = json.dumps(li)
            formated_lines.append(format_str(line['key'], li, tabs))

        elif line['status'] == 'not_same':
            v2 = line['value2']
            if type(line['value']) is dict:
                li = format_child(line['value'], tabs + 4)
            elif type(line['value2']) is dict:
                v2 = format_child(line['value2'], tabs + 4)
            formated_lines.append(format_str(line['key'], li, tabs, '-'))
            formated_lines.append(format_str(line['key'], v2, tabs, '+'))
            
        elif line['status'] == 'child':
            format_child_ = format_diff(li, tabs+4)
            formated_lines.append(format_str(line['key'], format_child_, tabs))

    formated_lines.append(' ' * (tabs - 4) + '}')
  
    return '\n'.join(formated_lines)


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
