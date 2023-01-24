import yaml
import json


def parse_data(data, format_):
    """Parse file. Supported types is JSON, YAML and YML."""
    if format_ == 'json':
        return json.loads(data)
    elif format_ == 'yaml' or format_ == 'yml':
        return yaml.safe_load(data)
    raise TypeError("Can't read because input data type is not supported")
