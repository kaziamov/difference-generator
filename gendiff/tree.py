def build_diff(data1, data2):
    """Make structure of differences for childs from two trees"""
    keys = sorted(data1.keys() | data2.keys())
    result = []
    for key in keys:
        status = {'key': key}
        if key not in data2:
            status.update(
                {'status': 'removed',
                 'value': data1[key]})

        elif key not in data1:
            status.update(
                {'status': 'added',
                 'value': data2[key]})

        elif type(data1[key]) == dict and type(data2[key]) == dict:
            childs_diff = build_diff(data1[key], data2[key])
            status.update(
                {'status': 'child',
                 'child': childs_diff})

        elif data1[key] == data2[key]:
            status.update(
                {'status': 'same',
                 'value': data1[key]})

        else:
            status.update({'status': 'updated',
                           'value': data1[key],
                           'value2': data2[key]})

        result.append(status)
    return result
