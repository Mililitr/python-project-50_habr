import os
import unittest
import yaml
from gendiff.parser import parse


class TestParse(unittest.TestCase):
    def test_parse_json(self):
        # Путь к файлу JSON в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')

        # Ожидаемый результат
        expected_result = {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        }

        # Проверка результата
        result = parse(filepath)
        self.assertEqual(result, expected_result)


    def test_parse_yaml(self):
        # Путь к файлу YAML в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')

        # Ожидаемый результат
        expected_result = {
            "language": "Why Python? Why not Sssssssssssnake+?",
            "version": "3.8 (eat five)",
            "author": {
                "name": "Duck",
                "email": "duck@example.com (this is a fake email)"
            },
            "repository": "myrepo (not to be confused with trash)"
        }

        # Проверка результата
        result = parse(filepath)
        self.assertEqual(result, expected_result)


    def test_parse_invalid_extension(self):
        # Путь к пустому файлу JSON в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'empty_file.json')

        # Проверка на возникновение ValueError
        with self.assertRaises(ValueError):
            parse(filepath)


    def test_parse_invalid_extension(self):
        # Путь к файлу с некорректным расширением в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.txt')

        # Проверка на возникновение ValueError при некорректном расширении файла
        with self.assertRaises(ValueError):
            parse(filepath)


    def test_parse_invalid_json(self):
        # Путь к файлу с некорректным JSON содержимым в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'invalid_file.json')

        # Проверка на возникновение ValueError при некорректном JSON содержимом
        with self.assertRaises(ValueError):
            parse(filepath)


    def test_parse_invalid_yaml(self):
        # Путь к файлу с некорректным YAML содержимым в fixtures
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'invalid_file.yml')

        # Проверка на возникновение ScannerError при некорректном YAML содержимом
        with self.assertRaises(yaml.scanner.ScannerError):
            parse(filepath)


if __name__ == '__main__':
    unittest.main()
