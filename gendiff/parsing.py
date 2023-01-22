# Import third-patry modules
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Import build-in modules
import json


# Import local modules


def parse_data(data, format_):
    """Parse file. Supported types is JSON, YAML and YML."""
    load_options = {
        'json': parse_json,
        'yaml': parse_yaml,
        'yml': parse_yaml,
    }
    action = load_options.get(format_, make_raise)
    return action(data)


def parse_json(data):
    """Open and read JSON. And return it."""
    return json.loads(data)


def parse_yaml(data):
    """Open and read YAML or YML. And return it."""
    return yaml.load(data, Loader=Loader)


def make_raise(*args):
    """Get raise for unsupported file type"""
    raise TypeError("Can't read because input data type is not supported")
