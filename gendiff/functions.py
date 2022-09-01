# Gendiff functionality

# Import build-in modules
import json


def open_file(path_to_file, format='json'):
    with open(path_to_file, 'r') as file_to_dict:
        dict = json.loads(file_to_dict)
        return dict

def open_two_files(files):
    # return map(open_file, files)
    return [open_file(file) for file in files]

def create_set(iterable_for_set):
    return set(iterable_for_set)

def get_union(list_of_dict):
    pass

def get_intersection_of_many(list_of_dict):
    pass



def generate_diff():
    pass

def print_diff():
    pass