import json
from gendiff.generate_diff import generate_diff


def test_generate_diff(tmp_path):
    # Проверяем, что функция корректно обрабатывает два файла в формате JSON
    file_path1 = tmp_path / "file1.json"
    file_path2 = tmp_path / "file2.json"
    file_path1.write_text(json.dumps({'host': 'localhost', 'proxy': '123.234.53.22', 'timeout': 50}))
    file_path2.write_text(json.dumps({'host': 'hexlet.io', 'timeout': 20, 'verbose': True}))
    expected = {
        'host': {'old_value': 'localhost', 'new_value': 'hexlet.io', 'status': 'updated'},
        'timeout': {'old_value': 50, 'new_value': 20, 'status': 'updated'},
        'proxy': {'old_value': '123.234.53.22', 'new_value': None, 'status': 'deleted'},
        'verbose': {'old_value': None, 'new_value': True, 'status': 'added'}
    }
    assert generate_diff(str(file_path1), str(file_path2)) == expected

    # Проверяем, что функция корректно обрабатывает два других файла в формате JSON
    file_path1 = 'tests/fixtures/file3.json'
    file_path2 = 'tests/fixtures/file4.json'
    with open(file_path1) as _, open(file_path2) as _:
        expected = '''{
            "common": {
                "setting1": {
                    "old_value": "Value 1",
                    "new_value": null,
                    "status": "deleted"
                },
                "setting2": {
                    "old_value": 200,
                    "new_value": 300,
                    "status": "updated"
                },
                "setting3": {
                    "old_value": true,
                    "new_value": false,
                    "status": "updated"
                },
                "setting6": {
                    "old_value": {
                        "key": "value"
                    },
                    "new_value": {
                        "key": "value",
                        "list": [
                            "elem1",
                            "elem2"
                        ]
                    },
                    "status": "updated"
                },
                "setting4": {
                    "old_value": null,
                    "new_value": "blah blah",
                    "status": "added"
                },
                "setting5": {
                    "old_value": {
                        "key5": "value5"
                    },
                    "new_value": {
                        "key5": "value5"
                    },
                    "status": "unchanged"
                }
            }
        }'''
