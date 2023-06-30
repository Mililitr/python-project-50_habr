def build_indent(depth):
    return " " * (depth * 4 - 2)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            indent = build_indent(depth + 1)
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{indent}  {key}: {formatted_value}")
        return "{{\n{}\n{}}}".format("\n".join(lines), build_indent(depth))
    elif isinstance(value, list):
        lines = []
        for val in value:
            indent = build_indent(depth + 1)
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{indent}- {formatted_value}")
        return "[\n{}\n{}]".format("\n".join(lines), build_indent(depth))
    return stringify(value, depth)


def stringify(data, depth):
    if isinstance(data, bool):
        return 'true' if data else 'false'
    if data is None:
        return 'null'
    if isinstance(data, dict):
        return format_value(data, depth)
    if isinstance(data, list):
        return format_value(data, depth)
    return str(data)


def format_dict(diff, depth=1):
    if not isinstance(diff, dict):
        return str(diff)

    lines = []
    for item in diff:
        key = item['key']
        status = item['status']
        value = item['value']
        indent = build_indent(depth)
        formatted_value = format_value(value, depth)

        if status == 'added':
            lines.append(f"{indent}+ {key}: {formatted_value}")
        elif status == 'removed':
            lines.append(f"{indent}- {key}: {formatted_value}")
        elif status == 'changed':
            old_value, new_value = value
            lines.append(f"{indent}- {key}: {format_value(old_value, depth)}")
            lines.append(f"{indent}+ {key}: {format_value(new_value, depth)}")
        elif status == 'unchanged':
            lines.append(f"{indent}  {key}: {formatted_value}")

    return "\n".join(lines)


def format_diff_as_stylish(diff):
    return "\n" + format_dict(diff) + "\n"
