import json


def format(data):
    def iter_format(data, depth=1):
        if isinstance(data, dict):
            result = ''
            for key, value in data.items():
                result += f'{"    " * depth}{key}: {iter_format(value, depth + 1)}\n'
            return f'{{\n{result}{"    " * (depth - 1)}}}'

        if isinstance(data, list):
            result = ''
            for item in data:
                result += f'{"    " * depth}- {iter_format(item, depth + 1)}\n'
            return f'[\n{result}{"    " * (depth - 1)}]'

        return json.dumps(data)

    return iter_format(data).rstrip()
