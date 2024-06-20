import json
import yaml
from pathlib import Path

def parse(data, file_format):
    if file_format == ".json":
        return json.loads(data)
    elif file_format in (".yml", ".yaml"):
        return yaml.safe_load(data)

def get_data(file_path):
    file_format = Path(file_path).suffix
    with open(file_path) as f:
        data = f.read()
        return parse(data, file_format)
