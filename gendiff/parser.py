import json
import yaml
import os


def parse(filepath):
    _, extension = os.path.splitext(filepath)
    with open(filepath, 'r') as file:
        if extension == '.json':
            return json.load(file)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError(f'Unknown file extension: {extension}')
