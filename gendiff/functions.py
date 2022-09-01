# Gendiff functionality

# Import build-in modules
import json


def open_file(path_to_file, format='json'):
    """
    Open file in choicen format.
    By default as JSON
    """
    with open(path_to_file, 'r') as file_to_dict:
        dict = json.loads(file_to_dict)
        return dict


def create_set(iterable_for_set):
    return set(iterable_for_set)


def get_union(set1, set2):
    return set1 | set2


def get_intersection_of_many(set1, set2):
    return set1 & set2


def generate_diff(file1, file2, format='json'):
    """
    Conveyor for generate diff
    for two files.
    """
    # return map(open_file, files)
    [open_file(file) for file in files]


def print_diff():
    pass