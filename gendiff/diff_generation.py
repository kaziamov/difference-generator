from gendiff.getting_data import get_data, get_format
from gendiff.parsing import parse_data
from gendiff.formatting import format_tree
from gendiff.tree import build_diff


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
