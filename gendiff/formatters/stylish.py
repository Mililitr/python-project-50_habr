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
        for key, (status, value) in diff.items():
            if status == "added":
                result.append(f"    {' ' * depth}+ {key}: {format_value(value, depth + 4)}")
            elif status == "deleted":
                result.append(f"    {' ' * depth}- {key}: {format_value(value, depth + 4)}")
            elif status == "updated":
                old_value, new_value = value
                result.append(f"    {' ' * depth}- {key}: {format_value(old_value, depth + 4)}")
                result.append(f"    {' ' * depth}+ {key}: {format_value(new_value, depth + 4)}")
            elif status == "nested":
                result.append(f"    {' ' * depth}{key}: {format_dict(value, depth + 4)}")
            else:
                result.append(f"    {' ' * depth}  {key}: {format_value(value, depth + 4)}")
        return "{\n" + "\n".join(result) + f"\n{' ' * depth}}}"

    return format_dict(diff)
