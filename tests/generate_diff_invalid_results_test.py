import os
import pytest
import yaml
from gendiff.generate_diff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_fixture(file_path):
    with open(file_path) as f:
        return f.read()

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        generate_diff("nonexistent_file1.json", "nonexistent_file2.json", format_name='json')

def test_invalid_file_path_2():
    with pytest.raises(FileNotFoundError):
        generate_diff("nonexistent_file2.yml", "nonexistent_file2.yml", format_name='yml')

def test_invalid_json_format():
    file_path1 = os.path.join(FIXTURES_PATH, 'invalid_file.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    with pytest.raises(ValueError):
        generate_diff(file_path1, file_path2, format_name='json')

def test_invalid_yml_format():
    file_path1 = os.path.join(FIXTURES_PATH, 'invalid_file.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    with pytest.raises(yaml.scanner.ScannerError):
        generate_diff(file_path1, file_path2, format_name='yml')