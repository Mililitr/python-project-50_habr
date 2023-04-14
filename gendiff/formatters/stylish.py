import os
from gendiff.parser import parse


SPACES = '    '
ADDED = '  + '
REMOVED = '  - '


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth + 1)
    else:
        return str(value)


def format_dict(diff, depth=0):
    if not isinstance(diff, dict):
        return str(diff)

    lines = []
    for key, value in diff.items():
        if isinstance(value, dict):
            value = format_dict(value, depth + 1)
            lines.append(f"{SPACES * (depth + 1)}{key.strip()}: {value}")
        elif value == "added":
            value = format_value(diff[key][1], depth + 1)
            lines.append(f"{ADDED}{SPACES * (depth + 1)}{key.strip()}: {value}")
        elif value == "deleted":
            value = format_value(diff[key][0], depth + 1)
            lines.append(f"{REMOVED}{SPACES * (depth + 1)}{key.strip()}: {value}")
        elif isinstance(value, tuple) and len(value) == 2:
            old_value, new_value = value
            old_value = format_value(old_value, depth + 1)
            new_value = format_value(new_value, depth + 1)
            lines.append(f"{REMOVED}{SPACES * (depth + 1)}{key.strip()}: {old_value}")
            lines.append(f"{ADDED}{SPACES * (depth + 1)}{key.strip()}: {new_value}")
        else:
            value = format_value(value, depth + 1)
            lines.append(f"{SPACES * (depth + 1)}{key.strip()}: {value}")

    return "\n".join(lines)


def format_diff_as_stylish(diff):
    if isinstance(diff, str):
        _, extension = os.path.splitext(diff)
        if extension in ('.yml', '.yaml'):
            diff = parse(diff)
        else:
            return str(diff)

    return format_dict(diff)
