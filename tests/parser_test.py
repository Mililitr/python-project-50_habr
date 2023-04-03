import os
import unittest
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


if __name__ == '__main__':
    unittest.main()

