from gendiff.parser import parse


class AddedDiff:
    def __init__(self, key, value, depth):
        self.key = key
        self.value = value
        self.depth = depth

    def format(self):
        return f"{build_indent(self.depth)}+ {self.key}: {format_value(self.value, self.depth)}"


class RemovedDiff:
    def __init__(self, key, value, depth):
        self.key = key
        self.value = value
        self.depth = depth

    def format(self):
        return f"{build_indent(self.depth)}- {self.key}: {format_value(self.value, self.depth)}"


class ChangedDiff:
    def __init__(self, key, old_value, new_value, depth):
        self.key = key
        self.old_value = old_value
        self.new_value = new_value
        self.depth = depth

    def format(self):
        lines = []
        lines.append(f"{build_indent(self.depth)}- {self.key}: {format_value(self.old_value, self.depth)}")
        lines.append(f"{build_indent(self.depth)}+ {self.key}: {format_value(self.new_value, self.depth)}")
        return "\n".join(lines)


class UnchangedDiff:
    def __init__(self, key, value, depth):
        self.key = key
        self.value = value
        self.depth = depth

    def format(self):
        return f"{build_indent(self.depth)}  {self.key}: {format_value(self.value, self.depth)}"


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
