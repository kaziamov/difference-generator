from gendiff.parsing import parse_data


def get_data():
    pass


def open_two_files(path_to_file1, path_to_file2):
    """Open two files and return it like dictionaries."""
    dict1 = parse_data(path_to_file1)
    dict2 = parse_data(path_to_file2)
    return dict1, dict2