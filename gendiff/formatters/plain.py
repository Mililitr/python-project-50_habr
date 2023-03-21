def format_diff_as_plain(diff, path=''):
    if isinstance(diff, str):
        return diff
    lines = []
    for key, value in diff.items():
        if isinstance(value, dict):
            lines.append(format_diff_as_plain(value, f"{path}{key}."))
        elif isinstance(value, list):
            lines.append(format_diff_as_plain(value, f"{path}{key}[{i}]."))
        else:
            if value is None:
                value = 'null'
            lines.append(f"Property '{path}{key}' was updated. From {value[0]} to {value[1]}")
    return "\n".join(lines)
