import json

def get_indent(level, spaces_per_level=4):
    """Return whitespaces like intend"""
    return ' ' * spaces_per_level * level


def format_diff(tree, level=0):
    """Formatting tree of differences from dictionary."""
    f = []
    key = tree.get('key')
    value = tree.get('value')
    value1 = tree.get('value1')
    value2 = tree.get('value2')
    child = tree.get('child')

    if tree['status'] == 'root':
        f.append('{\n')
        result = list(map(lambda x: format_diff(x, level + 1), child))
        f.extend(result)
        f.append('}')

    if tree['status'] == 'first_only':
        if type(value1) is list:
            value1 = format_diff(value1, level + 1)
        else:
            value1 = json.dumps(value1)
        f.append('  - {}: {}\n'.format(key, value1))

    if tree['status'] == 'second_only':

        f.append('  + {}: {}\n'.format(key, value2))

    if tree['status'] == 'same':
        if type(value) is list:
            value = format_diff(value, level + 1)
        else:
            value = json.dumps(value)
        f.append('    {}: {}\n'.format(key, value))

    if tree['status'] == 'not_same':
        if type(value1) is list:
            value1 = format_diff(value1, level + 1)
        elif type(value2) is list:
            value2 = format_diff(value2, level + 1)
        f.append('  - {}: {}\n'.format(key, value1))
        f.append('  + {}: {}\n'.format(key, value2))

    if tree['status'] == 'child':
        f.append('{\n')
        result = list(map(lambda x: format_diff(x, level + 1), child))
        f.extend(result)
        f.append('}\n')

    # f.append(get_indent(level) + '}')
    result = ''.join(f).replace('"', '')
    return result

def convert_to_str(line, level):
    if not isinstance(line, dict):
        return json.dumps(line)
    else:
        result = ''
        indent = get_indent(level + 1)
        for data in line:
            value = convert_to_str(line[data], level + 1)
            result += f'\n{indent}    {data}: {value}'
        return f'{{{result}\n{indent}}}'
