# Import build-in modules
import json


def _format_node_(node):
    """Format tree childs"""
    formatted_node = _jsonify_tree_(node)
    result = json.dumps(formatted_node)
    return result


def _jsonify_tree_(tree):
    """Format tree to json-like dictionary"""
    key = tree.get('key')

    status = tree.get('status')
    childs = tree.get('child')

    result = {}

    value = tree.get('value')
    value2 = tree.get('value2')

    if status == 'root' or status == 'child':
        for child in childs:
            formated_child = _jsonify_tree_(child)
            result.update(formated_child)

    if status == 'added':
        result.update({key: {"status": "added", "value": value}})

    if status == 'removed':
        result.update({key: {"status": "removed", "value": value}})

    if status == 'updated':
        result.update({key: {"status": status, "old_value": value, "new_value": value2}})

    if status == 'same':
        result.update({key: {"status": "same", "value": value}})

    return result
