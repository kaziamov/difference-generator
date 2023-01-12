import json


def _convert_to_string(data, indent):
    if type(data) is bool or data is None:
        return json.dumps(data)
    elif type(data) is dict:
        formatted_dict = []
        for x, y in data.items():
            key = x
            value = y
            if type(y) is dict:
                value = _convert_to_string(y, f'    {indent}')
            formatted_line = f'{indent}    {key}: {value}'
            formatted_dict.append(formatted_line)
        return '{\n' + '\n'.join(formatted_dict) + '\n' + indent + '}'
    else:
        return data


def _get_indent(level=0, spaces_count=4):
    if not level:
        return ''
    return ' ' * spaces_count * level


def _get_brakes(data, indent):
    return '{\n' + data + '\n' + indent + '}'


def formatting_tree(tree):
    result = _format_node_(tree)
    return result


def _format_node_(node, level=0):
    indent = _get_indent(level=level)

    key = node.get('key')
    status = node.get('status')
    childs = node.get('child')

    value = _convert_to_string(node.get('value'), indent=_get_indent(level+1))
    value2 = _convert_to_string(node.get('value2'), indent=_get_indent(level+1))

    if status == 'root':
        strings = [_format_node_(child, level=0) for child in childs]
        result = _get_brakes(
            '\n'.join(strings), f'{indent}'
        )

    if status == 'added':
        result = f'{indent}  + {key}: {value}'

    if node['status'] == 'removed':
        result = f'{indent}  - {key}: {value}'

    if status == 'updated':
        strings = [f'{indent}  - {key}: {value}',
                   f'{indent}  + {key}: {value2}']
        result = '\n'.join(strings)

    if status == 'same':
        result = f'{indent}    {key}: {value}'

    if status == 'child':
        strings = [_format_node_(child, level + 1) for child in childs]
        value = _get_brakes(
            '\n'.join(strings), f'    {indent}'
        )
        result = f'{indent}    {key}: {value}'

    return result
