def format_diff_as_plain(diff):
    def plain_value(value):
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, str):
            return f"'{value}'"
        return str(value)

    lines = []
    for key, (status, value) in diff.items():
        if status == 'added':
            lines.append(f"Property '{key}' was added with value: {plain_value(value)}")
        elif status == 'deleted':
            lines.append(f"Property '{key}' was removed")
        elif status == 'updated':
            old_value, new_value = value
            lines.append(f"Property '{key}' was updated. From {plain_value(old_value)} to {plain_value(new_value)}")
    return '\n'.join(lines)
