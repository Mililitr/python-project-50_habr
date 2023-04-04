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
    expected_result = json.loads(read_fixture(
        os.path.join(FIXTURES_PATH, 'json_result.txt')))
    result = generate_diff(file_path1, file_path2, output_format='json')
    assert json.loads(result) == json.loads(expected_result)


def test_flat_diff_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'plain_result.txt')).strip() + '\n'
    result = generate_diff(file_path1, file_path2, output_format='plain')
    assert sorted(result.splitlines()) == sorted(expected_result.splitlines())


def test_nested_diff_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'nested/nested_file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'nested/nested_file2.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'nested_result.txt'))
    result = generate_diff(file_path1, file_path2, output_format='plain')
    assert sorted(result.splitlines()) == sorted(expected_result.splitlines())


def test_stylish_diff_json():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.json')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.json')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'stylish_result.txt'))
    result = generate_diff(file_path1, file_path2, output_format='stylish')
    assert sorted(result.splitlines()) == sorted(expected_result.splitlines())
