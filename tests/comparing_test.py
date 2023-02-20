import os
import pytest
from gendiff.generate_diff import generate_diff


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_name):
    with open(os.path.join(FIXTURES_PATH, file_name)) as f:
        return f.read()


def test_generate_diff_plain_files():
    file1 = 'file1.json'
    file2 = 'file2.json'
    expected_output = read_fixture('expected_plain_diff.txt').strip()
    assert generate_diff(os.path.join(FIXTURES_PATH, file1), os.path.join(FIXTURES_PATH, file2)) == expected_output


def test_generate_diff_nested_files():
    file1 = 'file1.json'
    file2 = 'file2.json'
    expected_output = read_fixture('expected_nested_diff.txt').strip()
    assert generate_diff(os.path.join(FIXTURES_PATH, file1), os.path.join(FIXTURES_PATH, file2)) == expected_output
