import json
import unittest
from gendiff.cli import generate_diff

class TestGenerateDiff(unittest.TestCase):
    def test_generate_diff_plain_files(self):
        # Проверяем, что функция правильно сравнивает два плоских файла
        file1_path = 'tests/fixtures/file1.json'
        file2_path = 'tests/fixtures/file2.json'
        expected_output = '{\n  "follow": false\n- "host": "hexlet.io"\n+ "timeout": 50\n- "proxy": "123.234.53.22"\n+ "verbose": true\n}'
        self.assertEqual(generate_diff(file1_path, file2_path), expected_output)

    def test_generate_diff_nested_files(self):
        # Проверяем, что функция правильно сравнивает два вложенных файла
        file1_path = 'tests/fixtures/file3.json'
        file2_path = 'tests/fixtures/file4.json'
        expected_output = '{\n  "common": {\n    "setting1": "Value 1"\n-   "setting2": 200\n+   "setting3": {\n+     "key": "value"\n+   }\n-   "setting3": {\n-     "key": "value"\n-   }\n    "setting6": {\n      "key": "value"\n+     "ops": "vops"\n    }\n  }\n  "group1": {\n-   "baz": "bas"\n+   "baz": "bars"\n    "foo": "bar"\n  }\n- "group2": {\n-   "abc": "12345"\n-   "deep": {\n-     "id": 45\n-   }\n- }\n+ "group3": {\n+   "fee": 100500\n+   "deep": {\n+     "id": {\n+       "number": 45\n+     }\n+   }\n+ }\n}'
        self.assertEqual(generate_diff(file1_path, file2_path), expected_output)

