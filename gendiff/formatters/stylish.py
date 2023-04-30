import os
from gendiff.parser import parse


def build_indent(depth):
    return " " * (depth * 4)


def format_diff_as_stylish(diff):
    def format_value(value, depth):
        if isinstance(value, dict):
            lines = []
            for key, inner_value in value.items():
                lines.append(f"{build_indent(depth + 1)}{key}: {format_value(inner_value, depth + 1)}")
            return "{{\n" + "\n".join(lines) + f"\n{build_indent(depth)}}}"
        else:
            return str(value)

    def format_dict(diff, depth=1):
        if not isinstance(diff, dict):
            return str(diff)
        lines = []
        for key, (status, value) in diff.items():
            if status == "added":
                lines.append(f"{build_indent(depth)}+ {key}: {format_value(value, depth)}")
            elif status == "removed":
                lines.append(f"{build_indent(depth)}- {key}: {format_value(value, depth)}")
            elif status == "changed":
                old_value, new_value = value
                lines.append(f"{build_indent(depth)}- {key}: {format_value(old_value, depth)}")
                lines.append(f"{build_indent(depth)}+ {key}: {format_value(new_value, depth)}")
            else:
                lines.append(f"{build_indent(depth)}  {key}: {format_value(value, depth)}")
        return "{\n" + "\n".join(lines) + "\n" + build_indent(depth - 1) + "}"
    return format_dict(diff)
