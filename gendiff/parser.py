import json
import yaml
from pathlib import Path

def parse(file_path, file_format):
    with open(file_path, 'r') as file:
        if file_format == '.json':
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON file: {file_path}")
        elif file_format in ('.yml', '.yaml'):
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError:
                raise yaml.scanner.ScannerError(f"Invalid YAML file: {file_path}")
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

def get_data(file_path):
    file_format = Path(file_path).suffix
    return parse(file_path, file_format)