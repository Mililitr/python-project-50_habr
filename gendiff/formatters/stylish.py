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
    for key, (status, value) in diff.items():
        if status == "added":
            diff_obj = AddedDiff(key, value, depth)
        elif status == "removed":
            diff_obj = RemovedDiff(key, value, depth)
        elif status == "changed":
            old_value, new_value = value
            diff_obj = ChangedDiff(key, old_value, new_value, depth)
        else:
            diff_obj = UnchangedDiff(key, value, depth)
        lines.append(diff_obj.format())
    return "{\n" + "\n".join(lines) + "\n" + build_indent(depth - 1) + "}"


def format_diff_as_stylish(diff):
    return format_dict(diff)
