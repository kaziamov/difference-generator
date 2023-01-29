import argparse

from gendiff.formatting import get_formats


def get_args():
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
    return parser.parse_args()
