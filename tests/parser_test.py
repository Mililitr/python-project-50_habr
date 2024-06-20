import os
import unittest
import yaml
from gendiff.parser import parse

class TestParse(unittest.TestCase):

    def test_parse_invalid_yaml(self):
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'invalid_file.yml')
        with self.assertRaises(yaml.scanner.ScannerError):
            parse(filepath, '.yml')

    def test_parse_json(self):
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
        expected_result = {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        }
        result = parse(filepath, '.json')
        self.assertEqual(result, expected_result)

    def test_parse_yaml(self):
        filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
        expected_result = {
            "language": "Why Python? Why not Sssssssssssnake+?",
            "version": "3.8 (eat five)",
            "author": {
                "name": "Duck",
                "email": "duck@example.com (this is a fake email)"
            },
            "repository": "myrepo (not to be confused with trash)"
        }
        result = parse(filepath, '.yml')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()