def format_diff_as_plain(diff):
    def format_value(value):
        if isinstance(value, dict) or isinstance(value, list):
            return "[complex value]"
        elif value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value)

    def node_format(node, ancestry=''):
        if isinstance(node, str):
            return node  # If the node is a string, return it as is

        key = node.get('key')
        status = node.get('status')
        if status is None:
            return ""  # Return an empty string to skip nodes with unknown status
        property_name = f"{ancestry}{key}"

        if status == 'added':
            return f"Property '{property_name}' was added with value: {format_value(node['value'])}\n"
        elif status == 'removed':
            return f"Property '{property_name}' was removed\n"
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            return f"Property '{property_name}' was changed. From {old_value} to {new_value}\n"
        elif status == 'unchanged':
            return ""
        elif status == 'nested':
            children = node.get('children', [])
            nodes = [node_format(child, f"{property_name}.") for child in children]
            return ''.join(node for node in nodes if node)  # Skip empty strings and join the results
        else:
            raise Exception(f"Unknown status: {status}")

    return ''.join(node_format(node) for node in diff)
