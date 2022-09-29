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
    result = '\n'.join(compare_files(open_two_files(path_to_file1, path_to_file2))).replace('"', "").replace("'", "")
    return '{\n' + result + '\n}'


def open_two_files(path_to_file1, path_to_file2):
    dict1 = read_and_parse(path_to_file1)
    dict2 = read_and_parse(path_to_file2)
    return dict1, dict2


def compare_files(two_dictionaries_in_tuple):
    dict1, dict2 = two_dictionaries_in_tuple
    set1, set2 = set(dict1), set(dict2)

    differences = []
    for key in sorted(set1 | set2):

        if key in set1 and key in set2:
            value1 = json.dumps(dict1[key])
            value2 = json.dumps(dict2[key])
            if dict1[key] == dict2[key]:
                differences.append(f'    {key}: {value1}')
            else:
                # differences.append(compare_files(dict1[key], dict2[key]))
                differences.append(f'  - {key}: {value1}')
                differences.append(f'  + {key}: {value2}')

        elif key in set1:
            value1 = json.dumps(dict1[key])
            differences.append(f'  - {key}: {value1}')
        elif key in set2:
            value2 = json.dumps(dict2[key])
            differences.append(f'  + {key}: {value2}')

    return differences


if __name__ == '__main__':
    main()
