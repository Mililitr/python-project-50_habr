import json
import unittest
from gendiff.cli import generate_diff

class TestGenerateDiff(unittest.TestCase):
    def test_generate_diff_plain_files(self):
        # Проверяем, что функция правильно сравнивает два плоских файла
        file1_path = 'tests/fixtures/file1.json'
        file2_path = 'tests/fixtures/file2.json'
        expected_output = '''{
- follow: false
  host: "hexlet.io"
- proxy: "123.234.53.22"
+ timeout: 50
+ verbose: true
}'''
        self.assertMultiLineEqual(generate_diff(file1_path, file2_path), expected_output)

    def test_generate_diff_nested_files(self):
        # Проверяем, что функция правильно сравнивает два вложенных файла
        file1_path = 'tests/fixtures/file3.json'
        file2_path = 'tests/fixtures/file4.json'
        expected_output = '''{
    common: {
        setting1: "Value 1"
-       setting2: 200
+       setting3: {
+           key: value
+       }
+       setting4: "value4"
    }
-   group1: {
-       abc: 12345
-       def: {
-           ghi: 67890
-       }
-   }
+   group2: {
+       abc: 54321
+       def: {
+           ghi: 9876
+       }
+       group3: {
+           key1: value1
+           key2: {
+               key3: value3
+           }
+       }
+   }
}'''
        self.assertMultiLineEqual(generate_diff(file1_path, file2_path), expected_output)

if __name__ == "__main__":
    unittest.main()
