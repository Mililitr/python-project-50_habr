import json
import yaml
from pathlib import Path
from gendiff.formatters.stylish import format_diff_as_stylish
from gendiff.formatters.plain import format_diff_as_plain
from gendiff.formatters.as_json import format_diff_as_json


def parse(data, file_format):
    if file_format == ".json":
        return json.loads(data)
    elif file_format in (".yml", ".yaml"):
        return yaml.safe_load(data)


def get_data(file_path):
    file_format = Path(file_path).suffix
    with open(file_path) as f:
        data = f.read()
        return parse(data, file_format)


def build_diff(file1, file2):
    diff = []
    for key in sorted(set(file1) | set(file2)):
        if key not in file2:
            diff.append({
                "key": key,
                "status": 'removed',
                "value": file1[key],
            })
        elif key not in file1:
            diff.append({
                "key": key,
                "status": 'added',
                "value": file2[key]
            })
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = build_diff(file1[key], file2[key])
            if nested_diff:
                diff.append({
                    "key": key,
                    "status": 'nested',
                    "children": nested_diff
                })
        elif file1[key] == file2[key]:
            diff.append({
                "key": key,
                "status": 'unchanged',
                "value": file1[key]
            })
        else:
            diff.append({
                "key": key,
                "status": 'changed',
                "old_value": file1[key],
                "new_value": file2[key]
            })
    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = build_diff(data1, data2)
    if format_name == 'stylish':
        return format_diff_as_stylish(diff)
    elif format_name == "plain":
        return format_diff_as_plain(diff)
    elif format_name == 'json':
        return format_diff_as_json(diff)
