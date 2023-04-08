import json
from gendiff.formatters import stylish
from gendiff.generat_diff import generate_diff

def format(data, formatter='stylish'):
    if formatter == 'stylish':
        return stylish.format(data)
    elif formatter == 'json':
        return json.dumps(data, indent=4)
    else:
        raise ValueError(f'Unknown formatter: {formatter}')


__all__ = ['format']
