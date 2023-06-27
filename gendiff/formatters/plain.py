def format_diff_as_plain(diff):
    def format_value(value):
        if isinstance(value, dict) or isinstance(value, list):
            return '[complex value]'
        elif value is None:
            return 'null'
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value)

    lines = []
    for node in diff:
        key = node['key']
        status = node['status']
        if 'value' in node:
            value = format_value(node['value'])
        else:
            value = None
        if status == 'added':
            lines.append(f"Property '{key}' was added with value: '{value}'")
        elif status == 'removed':
            lines.append(f"Property '{key}' was removed")
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{key}' was changed. From '{old_value}' to '{new_value}'")
        elif status == 'unchanged':
            continue
        elif status == 'nested':
            lines += format_diff_as_plain(node['value'])
    return '\n'.join(lines)
