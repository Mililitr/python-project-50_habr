import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)

    keys = sorted(file1.keys() | file2.keys())

    diff = dict()

    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff[key] = {'value': file1[key], 'type': 'unchanged'}
            else:
                diff[key] = {'value1': file1[key], 'value2': file2[key], 'type': 'changed'}
        elif key in file1:
            diff[key] = {'value': file1[key], 'type': 'removed'}
        else:
            diff[key] = {'value': file2[key], 'type': 'added'}

    return json.dumps(diff, indent=4)
