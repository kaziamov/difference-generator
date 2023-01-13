# Import build-in modules
import json


# def _convert_to_string(data):
#     """Convert data to string format"""
#     if type(data) is bool or data is None:
#         return json.dumps(data)
#     elif type(data) is dict:
#         return '[complex value]'
#     else:
#         return data



def _format_node_(node):
    """Format tree childs"""
    formatted_node = _jsonify_tree_(node)
    result = json.dumps(formatted_node)
    return result


def _jsonify_tree_(tree):

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
        result.update({key:
            {"status": "added",
             "value": value}
        })


    if status == 'removed':
        result.update({key:
            {"status": "removed",
             "value": value}
        })


    if status == 'updated':
        result.update({key:
            {"status": status,
             "old_value": value,
             "new_value": value2}
        })


    if status == 'same':
        result.update({key:
            {"status": "same",
             "value": value}
        })

    # if node['status'] == 'removed':
    #     result = f"Property '{key}' was removed"

    # if status == 'updated':
    #     result = f"Property '{key}' was updated. From {value} to {value2}"

    # if status == 'child':
    #     strings = [_format_node_(child, key) for child in childs if child]
    #     truly_strings = [string for string in strings if string]
    #     result = '\n'.join(truly_strings)

    return result
