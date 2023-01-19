# Build-in modules
from pathlib import PurePosixPath

# Local modules
from gendiff.parsing import parse_data


def get_data(data):
    datatype = get_format(data)
    if data:
        data = open_and_read_file(data)
    return data, datatype


def get_format(file):
    """Return suffix of file."""
    return PurePosixPath(file).suffix[1:]


def open_and_read_file(path_to_file):
    """Open and read file."""
    with open(path_to_file, 'r', encoding="utf-8") as file:
        return file.read()
