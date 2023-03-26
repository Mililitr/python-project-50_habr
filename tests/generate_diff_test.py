import os
import pytest
import json
from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import format_diff_as_stylish
from gendiff.formatters.plain import format_diff_as_plain
from gendiff.formatters.as_json import format_diff_as_json
import textwrap

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
    assert json.loads(result) == expected_result


def test_flat_diff_plain():
    file_path1 = os.path.join(FIXTURES_PATH, 'file1.yml')
    file_path2 = os.path.join(FIXTURES_PATH, 'file2.yml')
    expected_result = read_fixture(os.path.join(FIXTURES_PATH, 'plain_result.txt')).strip() + '\n'
