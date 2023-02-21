import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        dict1 = json.load(f1)
        dict2 = json.load(f2)

    diff = {}
    keys = dict1.keys() | dict2.keys()
    for key in sorted(keys):
        if key in dict1 and key not in dict2:
            diff[f'- {key}'] = dict1[key]
        elif key in dict2 and key not in dict1:
            diff[f'+ {key}'] = dict2[key]
        elif dict1[key] != dict2[key]:
            diff[f'- {key}'] = dict1[key]
            diff[f'+ {key}'] = dict2[key]
        else:
            diff[f'  {key}'] = dict1[key]

    return diff
