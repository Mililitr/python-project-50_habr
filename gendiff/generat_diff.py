import os
from gendiff.formatters.stylish import format_diff_as_stylish
from gendiff.formatters.plain import format_diff_as_plain
from gendiff.formatters.as_json import format_diff_as_json
from gendiff.parser import parse


def make_diff(data1, data2, parent=None):
    """
    Сравнивает два словаря и формирует результат.

    Args:
        data1: первый словарь.
        data2: второй словарь.
        parent: родительский ключ.

    Returns:
        Результат сравнения в виде списка словарей.
    """
    if parent is None:
        parent = []
    diff = []
    for key in data1.keys() | data2.keys():
        path = [*parent, key]
        path_str = '.'.join(str(p) for p in path)
        if key not in data1:
            diff.append({'path': path_str, 'status': 'added', 'value': data2[key]})
        elif key not in data2:
            diff.append({'path': path_str, 'status': 'deleted', 'value': data1[key]})
        elif data1[key] != data2[key]:
            diff.append({'path': path_str, 'status': 'updated', 'value': (data1[key], data2[key])})
        elif isinstance(data1[key], (dict, list)) and isinstance(data2[key], (dict, list)):
            diff.extend(make_diff(data1[key], data2[key], path))
        else:
            diff.append({'path': path_str, 'status': 'unchanged', 'value': data1[key]})
    return diff


def generate_diff(filepath1, filepath2, output_format='stylish'):
    filepath1_abs = os.path.abspath(filepath1)
    filepath2_abs = os.path.abspath(filepath2)
    diff = make_diff(dict(parse(filepath1_abs)), dict(parse(filepath2_abs)))
    if output_format == 'stylish':
        return format_diff_as_stylish(diff)
    elif output_format == 'plain':
        return format_diff_as_plain(diff).replace('\n\n', '\n').rstrip()
    elif output_format == 'json':
        return format_diff_as_json(diff)
    else:
        raise ValueError(f'Unknown format: {output_format}')
