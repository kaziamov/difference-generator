# Import third-patry modules
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Import build-in modules
import json
from pathlib import PurePosixPath

# Import local modules


def get_format(file):
    """Return suffix of file."""
    return PurePosixPath(file).suffix


def read_and_parse(path_to_file):
    """Parse file. Supported types is JSON, YAML and YML."""
    load_options = {
        'json': load_json,
        'yaml': load_yaml,
        'yml': load_yaml,
        'error': make_raise,
    }
    format = get_format(path_to_file)
    action = load_options.get(format[1:], 'error')
    return action(path_to_file)


def load_json(path_to_file):
    """Open and read JSON. And return it."""
    with open(path_to_file, 'r') as file:
        return json.load(file)


def load_yaml(path_to_file):
    """Open and read YAML or YML. And return it."""
    with open(path_to_file, 'r') as file:
        return yaml.load(file, Loader=Loader)


def make_raise(*args):
    raise "Can't read because file type is not supported"
