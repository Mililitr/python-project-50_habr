import json
import yaml
import os
from .formatters.stylish import format_diff_as_stylish
from .formatters.plain import format_diff_as_plain
from .formatters.json import format_diff_as_json
from gendiff.parser import parse

def make_diff(data1, data2, parent=""):
    """Сравнивает два словаря и формирует результат.

    Args:
        data1: первый словарь.
        data2: второй словарь.
        parent: родительский ключ.

    Returns:
        Результат сравнения в виде словаря.
    """
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        path = f"{parent}.{key}" if parent else key
        if key not in data1:
            diff[path] = ("added", data2[key])
        elif key not in data2:
            diff[path] = ("deleted", data1[key])
        elif data1[key] == data2[key]:
            diff[path] = ("unchanged", data1[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.update(make_diff(data1[key], data2[key], path))
        else:
            diff[path] = ("updated", (data1[key], data2[key]))
    return diff


def generate_diff(filepath1, filepath2, output_format='stylish'):
    filepath1_abs = os.path.abspath(filepath1)
    filepath2_abs = os.path.abspath(filepath2)
    diff = make_diff(parse(filepath1_abs), parse(filepath2_abs))
    if output_format == 'stylish':
        return format_diff_as_stylish(diff)
    elif output_format == 'plain':
        return format_diff_as_plain(diff)
    elif output_format == 'json':
        return format_diff_as_json(diff)
    else:
        raise ValueError(f'Unknown format: {output_format}')
