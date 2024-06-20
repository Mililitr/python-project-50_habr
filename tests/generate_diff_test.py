import os
import json
from gendiff.generate_diff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')

def read_fixture(file_path):
    with open(file_path) as f:
        return f.read()

def test_flat_diff_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_result = json.loads(read_fixture(os.path.join(FIXTURES_PATH, 'json_result.txt')))
    result = generate_diff(file_path1, file_path2, format_name='json')
    assert result == expected_result


def test_flat_diff_yml_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = json.loads(read_fixture(
        os.path.join(FIXTURES_PATH, 'json_yml_result.txt')))
    result = generate_diff(file_path1, file_path2, format_name='json')
    assert result == expected_result


def test_flat_diff_jsonyml_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = json.loads(read_fixture(
        os.path.join(FIXTURES_PATH, 'json_jsonyml_result.txt')))
    result = generate_diff(file_path1, file_path2, format_name='json')
    assert result == expected_result


def test_flat_diff_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'plain_result.txt')).strip() + '\n'
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result == expected_result


def test_flat_diff_json_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'plain_json_result.txt')).strip() + '\n'
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result == expected_result


def test_flat_diff_jsonyml_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'plain_jsonyml_result.txt')).strip() + '\n'
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result == expected_result


def test_nested_diff_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'nested/nested_file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'nested/nested_file2.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'nested_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result == expected_result


def test_nested_diff_yml_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'nested/nested_file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'nested/nested_file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'nested_yml_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result == expected_result


def test_stylish_diff_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'stylish_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='stylish')
    assert result == expected_result


def test_stylish_diff_yml_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'stylish_yml_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='stylish')
    assert result == expected_result


def test_stylish_same_files_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file1.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'stylish_same_json_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='stylish')
    assert result == expected_result


def test_stylish_files_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file1.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'stylish_yml_json_result.txt'))
    result = generate_diff(file_path1, file_path2, format_name='stylish')
    assert result == expected_result
