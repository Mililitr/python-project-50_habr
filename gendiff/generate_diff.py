import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1:
        data1 = json.load(file1)
    with open(file_path2) as file2:
        data2 = json.load(file2)
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        if key not in data1:
            diff[key] = {
                "old_value": None,
                "new_value": data2[key],
                "status": "added"
            }
        elif key not in data2:
            diff[key] = {
                "old_value": data1[key],
                "new_value": None,
                "status": "deleted"
            }
        elif data1[key] == data2[key]:
            diff[key] = {
                "old_value": data1[key],
                "new_value": data2[key],
                "status": "unchanged"
            }
        else:
            diff[key] = {
                "old_value": data1[key],
                "new_value": data2[key],
                "status": "updated"
            }
    return diff
