import json
import yaml
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


def test_generate_diff_yaml():
    expected_output = "{\n"\
                      "  - author:\n"\
                      "      email: duck@example.com (this is a fake email)\n"\
                      "      name: Duck\n"\
                      "    language: Why Python? Why not Sssssssssssnake+?\n"\
                      "    repository: myrepo (not to be confused with trash)\n"\
                      "    version: 3.8 (eat five)\n"\
                      "  + author:\n"\
                      "      email: duck@example.com (this is not a fake email)\n"\
                      "      name: Not a Duck\n"\
                      "    language: Why Python? Why not Sssssssssssnake+?\n"\
                      "    repository: myrepo (not to be confused with trash)\n"\
                      "    version: 3.8 (eat five)\n"\
                      "}"
    file_path1 = 'tests/fixtures/file3.yaml'
    file_path2 = 'tests/fixtures/file1.yml'
    assert generate_diff(file_path1, file_path2) == expected_output


def test_generate_diff_yml():
    expected_output = "{\n"\
                      "  - Ducks: Are cool creatures\n"\
                      "    I_like: big ducks and I cannot lie\n"\
                      "    favorite_color: yellow\n"\
                      "    number_of_ducks: 99\n"\
                      "  + Ducks2: Are cool creatures 2\n"\
                      "    I_like: small ducks and I cannot lie\n"\
                      "    favorite_color: white\n"\
                      "    number_of_ducks: 5\n"\
                      "}"
    file_path1 = 'tests/fixtures/file2.yml'
    file_path2 = 'tests/fixtures/file5.yml'
    assert generate_diff(file_path1, file_path2) == expected_output

def test_generate_diff_same_data_yaml():
    file_path1 = 'tests/fixtures/file1.yml'
    file_path2 = 'tests/fixtures/file3.yaml'
    expected_output = "{\n}"
    assert generate_diff(file_path1, file_path2) == expected_output
def test_generate_diff_empty_files_yaml():
    file_path1 = 'tests/fixtures/empty_file.yml'
    file_path2 = 'tests/fixtures/empty_file.yaml'
    expected_output = "{\n}"
    assert generate_diff(file_path1, file_path2) == expected_output
