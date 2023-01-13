#!/usr/bin/env python

# Import build-in modules
import argparse

# Import local modules
from gendiff.scripts.parsing import read_and_parse
from gendiff.scripts.formatting import format_tree, get_formats

def main():
    """Сreate command-line interface for program"""
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Program for compare two files and print difference. Supported file types: JSON and YAML/YML')
    parser.add_argument('first_file',
                        help='First file to compare')
    parser.add_argument('second_file',
                        help='Second file to compare')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        default='stylish',
                        choices=get_formats(),
                        help='Format style to output ("stylish" by default)')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


def generate_diff(path_to_file1, path_to_file2, style="stylish"):
    """Generate tree of difference from two dictionaries."""
    gendiff = _create_root(read_and_parse(path_to_file1), read_and_parse(path_to_file2))
    result = format_tree(gendiff, style)
    return result


def open_two_files(path_to_file1, path_to_file2):
    """Open two files and return it like dictionaries."""
    dict1 = read_and_parse(path_to_file1)
    dict2 = read_and_parse(path_to_file2)
    return dict1, dict2


def _create_root(data1, data2):
    """Make differences for root segment from two trees"""
    return {'status': 'root', 'child': make_diff(data1, data2)}


def make_diff(data1, data2):
    """Make structure of differences for childs from two trees"""
    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        status = {'key': key}
        if key not in data2:
            status.update(
                {'status': 'removed',
                 'value': data1[key]})

        elif key not in data1:
            status.update(
                {'status': 'added',
                 'value': data2[key]})

        elif type(data1[key]) == dict and type(data2[key]) == dict:
            childs_diff = make_diff(data1[key], data2[key])
            status.update(
                {'status': 'child',
                 'child': childs_diff})

        elif data1[key] == data2[key]:
            status.update(
                {'status': 'same',
                 'value': data1[key]})

        else:
            status.update({'status': 'updated',
                           'value': data1[key],
                           'value2': data2[key]})

        result.append(status)
    return result
