#!/usr/bin/env python

# Import local modules
from gendiff.receiving import get_data, get_format
from gendiff.parsing import parse_data
from gendiff.formatting import format_tree
from gendiff.cli import get_args
# from gendiff.receiving import get_data


def main():
    """Create and print diff from arguments"""
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


def generate_diff(path_to_data1, path_to_data2, style="stylish"):
    """Generate tree of difference from two data files."""
    format1 = get_format(path_to_data1)
    format2 = get_format(path_to_data2)
    data1 = get_data(path_to_data1)
    data2 = get_data(path_to_data2)
    gendiff = _create_root(parse_data(data1, format1), parse_data(data2, format2))
    result = format_tree(gendiff, style)
    return result


def _create_root(data1, data2):
    """Make differences for root segment from two trees"""
    return {'status': 'root', 'child': build_diff(data1, data2)}


def build_diff(data1, data2):
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
            childs_diff = build_diff(data1[key], data2[key])
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
