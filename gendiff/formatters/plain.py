# Import build-in modules
import json


def _convert_to_string(data):
    """Convert data to string format"""
    if type(data) is bool or data is None:
        return json.dumps(data)
    elif type(data) is dict:
        return '[complex value]'
    elif type(data) is int:
        return data
    else:
        return f"'{data}'"


def _format_node_(node, parent=''):
    """Format tree childs"""
    result = None
    if parent:
        parent = f"{parent}."
    key = "{}{}".format(parent, node.get('key', ''))

    status = node.get('status')
    childs = node.get('child')

    value = _convert_to_string(node.get('value'))
    value2 = _convert_to_string(node.get('value2'))

    if status == 'root':
        strings = [_format_node_(child) for child in childs]
        truly_strings = [string for string in strings if string]
        result = '\n'.join(truly_strings)

    if status == 'added':
        result = f"Property '{key}' was added with value: {value}"

    if node['status'] == 'removed':
        result = f"Property '{key}' was removed"

    if status == 'updated':
        result = f"Property '{key}' was updated. From {value} to {value2}"

    if status == 'child':
        strings = [_format_node_(child, key) for child in childs if child]
        truly_strings = [string for string in strings if string]
        result = '\n'.join(truly_strings)

    return result
