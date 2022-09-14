# Import build-in modules
import json
import pathlib

# Import third-part modules
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def check_format(path_to_file):
    """Check file extension and return format like '.txt'"""
    file_format = pathlib.Path(path_to_file).suffix
    return file_format


def read_file(path_to_file):
    """Read file for specific format.
    Сompatibility witj json/yaml/yml.
    On another one return Exception"""

    format = check_format(path_to_file)
    func = FORMATS.get(format[1:], 'error')

    with open(path_to_file, 'r') as file:
        return func(file)


def parse_json(file):
    return json.load(file)


def parse_yaml(file):
    return yaml.load(file, Loader=Loader)


def make_error(file):
    raise Exception("Incorrect file extension")


FORMATS = {
    'json': parse_json,
    'yml': parse_yaml,
    'yaml': parse_yaml,
    'error': make_error,
}
