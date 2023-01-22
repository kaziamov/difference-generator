# Build-in modules
from pathlib import PurePosixPath


def get_data(data):
    if type(data) != 'str':
        data = open_and_read_file(data)
    return data


def get_format(file):
    """Return suffix of file."""
    return PurePosixPath(file).suffix[1:]


def open_and_read_file(path_to_file):
    """Open and read file."""
    with open(path_to_file, 'r', encoding="utf-8") as file:
        return file.read()
