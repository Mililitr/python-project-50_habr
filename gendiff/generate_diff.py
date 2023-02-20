import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1:
        data1 = json.load(file1)

    with open(file_path2) as file2:
        data2 = json.load(file2)

    diff = {}
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    common_keys = keys1.intersection(keys2)

    for key in common_keys:
        if data1[key] == data2[key]:
            diff[key] = (' ', data1[key])
        else:
            diff[key] = []
            diff[key].append(('-', data1[key]))
            diff[key + '.' + 'setting2'] = ('+', data2[key].get('setting2'))

    for key in keys1 - common_keys:
        diff[key] = ('-', data1[key])

    for key in keys2 - common_keys:
        diff[key] = ('+', data2[key])

    lines = []
    for key, value in sorted(diff.items()):
        if isinstance(value, list):
            for prefix, val in value:
                lines.append(f'{prefix} {key}: {json.dumps(val)}')
        else:
            prefix, value = value
            lines.append(f'{prefix} {key}: {json.dumps(value)}')

    return '{\n' + '\n'.join(lines) + '\n}'  
