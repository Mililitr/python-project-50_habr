def format_diff_as_plain(diff, path=''):
    result = []
    for key, (status, value) in diff.items():
        if status == 'added':
            result.append(f"Property '{path}{key}' was added with value: {value}")
        elif status == 'removed':
            result.append(f"Property '{path}{key}' was removed")
        elif status == 'modified':
            result.append(f"Property '{path}{key}' was updated. From '{value[0]}' to '{value[1]}'")
        elif status == 'unchanged':
            pass
        elif status == 'nested':
            result.append(format_diff_as_plain(value, path=f"{path}{key}."))
    return '\n'.join(result)
