import os
import yaml
import json
from gendiff.parser import parse


def format_diff_as_stylish(diff):
    def format_value(value, depth):
        if isinstance(value, dict):
            return format_dict(value, depth + 1)
        else:
            return str(value)

    def format_dict(diff, depth=0):
        if not isinstance(diff, dict):
            return str(diff)

        result = []
        for key, value in diff.items():
            if isinstance(value, dict):
                result.append(f"    {' ' * depth}{key}: {format_dict(value, depth + 4)}")
            elif len(value) == 2:
                old_value, new_value = value
                result.append(f"    {' ' * depth}- {key}: {format_value(old_value, depth + 4)}")
                result.append(f"    {' ' * depth}+ {key}: {format_value(new_value, depth + 4)}")
            elif value == 'added':
                result.append(f"    {' ' * depth}+ {key}: {format_value(diff[key][1], depth + 4)}")
            elif value == 'deleted':
                result.append(f"    {' ' * depth}- {key}: {format_value(diff[key][0], depth + 4)}")
            else:
                result.append(f"    {' ' * depth}  {key}: {format_value(value, depth + 4)}")
        return "{\n" + "\n".join(result) + f"\n{' ' * depth}}}"

    if isinstance(diff, str):
        _, extension = os.path.splitext(diff)
        if extension in ('.yml', '.yaml'):
            diff = parse(diff)
            return format_dict(diff)

    return format_dict(diff)
