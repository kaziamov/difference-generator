# Gendiff functionality

# Import local modules
from gendiff.functions import parsing


def open_file(path_to_file):
    """Open and read file for json or yaml formats"""
    return parsing.read_file(path_to_file)


def convert_to_set(iterable_for_set):
    """Convert iterable object to set"""
    return set(iterable_for_set)


def get_union(set1, set2):
    """Create union from two sets"""
    return set1 | set2


def get_intersection_of_many(set1, set2):
    """Create intersection for two sets"""
    return set1 & set2


def get_unique_in_set1(set1, set2):
    """Extract unique values for first set from two input sets"""
    return set1 - set2


def get_unique_in_set2(set1, set2):
    """Extract and return unique values for second set from two input sets"""
    return set2 - set1


def generate_diff(path_to_file1, path_to_file2, format='json'):
    """Conveyor for generate diff for two files."""
    dict1, dict2 = tuple(map(open_file, (path_to_file1, path_to_file2)))
    set1, set2 = tuple(map(convert_to_set, (dict1, dict2)))

    all_keys = sorted(get_union(set1, set2))

    unique_set1_keys = get_unique_in_set1(set1, set2)
    unique_set2_keys = get_unique_in_set2(set1, set2)

    result = []
    for key in all_keys:
        if key in unique_set1_keys:
            result.append(f'- {key}: {dict1[key]}')
        elif key in unique_set2_keys:
            result.append(f'+ {key}: {dict2[key]}')
        else:
            if dict1[key] == dict2[key]:
                result.append(f'  {key}: {dict1[key]}')
            else:
                result.append(f'- {key}: {dict1[key]}')
                result.append(f'+ {key}: {dict2[key]}')

    print_diff(result)


def print_diff(list_):
    """Output iterable on new line"""
    list_.insert(0, '{')
    list_.append('}')
    print(*list_, sep='\n')
