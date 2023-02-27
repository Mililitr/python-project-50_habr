import os
from gendiff.generate_diff import generate_diff


class TestGenerateDiff:
    def test_diff_json(self):
        path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
        path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
        expected_output_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'diff.json')
        with open(expected_output_path) as f:
            expected_output = f.read().strip()  # удаляем все пробельные символы
        assert generate_diff(path1, path2).strip() == expected_output  # удаляем все пробельные символы

    def test_diff_yaml(self):
        path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
        path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.yml')
        expected_output_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'diff.yml')
        with open(expected_output_path) as f:
            expected_output = f.read().strip()
        assert generate_diff(path1, path2).strip() == expected_output

    def test_diff_yaml_alternative(self):
        path1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file3.yaml')
        path2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file4.yaml')
        expected_output_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'diff.yaml')
        with open(expected_output_path) as f:
            expected_output = f.read().strip()
        assert generate_diff(path1, path2).strip() == expected_output
