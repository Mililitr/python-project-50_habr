import os
import pytest
from gendiff.generate_diff import generate_diff

@pytest.fixture
def filepath1():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')

@pytest.fixture
def filepath2():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

@pytest.fixture
def filepath3():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file3.yaml')

@pytest.fixture
def filepath4():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'file4.yaml')

@pytest.fixture
def empty_file1():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'empty_file.json')

@pytest.fixture
def empty_file2():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'empty_file2.json')

@pytest.fixture
def expected_result_json():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'json_result.txt')) as f:
        return f.read()

@pytest.fixture
def expected_result_plain():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'result_plain.txt')) as f:
        return f.read()

def test_generate_diff_for_json_files(filepath1, filepath2, expected_result_json):
    assert generate_diff(filepath1, filepath2) == expected_result_json

def test_generate_diff_json_output_formats(filepath1, filepath2):
    expected_result = '{\n  "key1": "value1",\n  "key2": "value2"\n}'
    assert generate_diff(filepath1, filepath2, output_format='json') == expected_result

def test_generate_diff_handles_plain_format(filepath3, filepath4, expected_result_plain):
    assert generate_diff(filepath3, filepath4, output_format='plain') == expected_result_plain + '\n'

def test_generate_diff_raises_ValueError(filepath1, filepath2):
    with pytest.raises(ValueError):
        generate_diff(filepath1, filepath2, output_format='invalid_format')

def test_generate_diff_raises_FileNotFoundError(filepath1):
    with pytest.raises(FileNotFoundError):
        filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'nonexistent_file.json')
        generate_diff(filepath1, filepath2)

def test_generate_diff_raises_TypeError(filepath1):
    with pytest.raises(TypeError):
        generate_diff(filepath1, 123)

def test_generate_diff_for_empty_files(empty_file1, empty_file2):
    expected_result = ''
    assert generate_diff(empty_file1, empty_file2) == expected_result

def test_generate_diff_for_one_empty_file(filepath1, empty_file1):
    expected_result = '{\n- "key1": "value1",\n- "key2": "value2"\n}'
    assert generate_diff(filepath1, empty_file1) == expected_result
