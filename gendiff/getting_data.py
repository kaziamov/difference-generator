from pathlib import PurePosixPath


def get_data(data):
    """Check input data type.
    Return data if there is string type (from request like example)
    or open and parse if it's file."""
    if type(data) != 'str':
        data = read_file(data)
    return data


def get_format(file):
    """Return suffix of file."""
    return PurePosixPath(file).suffix[1:]


def read_file(path_to_file):
    """Open and read file."""
    with open(path_to_file, 'r', encoding="utf-8") as file:
        return file.read()
