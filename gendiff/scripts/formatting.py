import json


def _convert_to_string(data):
    if type(data) is bool or data is None:
        return json.dumps(data)
    elif type(data) is dict:
        return map(lambda x: f'{x}')
    else:
        return data


def _get_intend(level=0, spaces_count=4):
    if not level:
        return ''
    return ' ' * spaces_count * level


def _get_brakes(data):
    return '{\n' + data + '\n}'


def formatting_tree(tree):
    result = _format_node_(tree)
    return result


def _format_node_(node, level=0):
    # print(f'node is {node}')
    intend = _get_intend(level=level)
    # print(f'intend is "{intend}", and level is {level}')

    key = node.get('key')
    # print(f'key is {key}')
    status = node.get('status')
    # print(f'status is {status}')
    childs = node.get('child')
    # print(f'child is {childs}')

    value = _convert_to_string(node.get('value'))
    # print(f'value is {value}')
    value1 = _convert_to_string(node.get('value1'))
    # print(f'value1 is {value1}')
    value2 = _convert_to_string(node.get('value2'))
    # print(f'value2 is {value2}')

    if status == 'root':
        print('root started')
        strings = [_format_node_(child, level=0) for child in childs]
        print(f'root strings is {strings}')
        result = _get_brakes(
            '\n'.join(strings)
        )
        # print(f'root result is {result}')

    if status == 'added':
        result = f'{intend}  + {key}: {value}'
        # print(f'added result is {result}')

    if node['status'] == 'removed':
        result = f'{intend}  - {key}: {value}'
        # print(f'removed result is {result}')

    if status == 'updated':
        strings = [f'{intend}  - {key}: {value1}',
                   f'{intend}  + {key}: {value2}']
        result = '\n'.join(strings)
        # print(f'updated result is {result}')

    if status == 'same':
        result = f'{intend}    {key}: {value}'
        # print(f'same result is {result}')

    if status == 'child':
        strings = [_format_node_(child, level + 1) for child in childs]
        # print(f'child strings is {strings}')
        result = '\n'.join(strings)
        # print(f'child result is {result}')

    # print(f'result is {result}')
    # print('______________________')
    return result
