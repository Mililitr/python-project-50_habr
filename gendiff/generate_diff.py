import json
import yaml
import os

FIXTURES_DIR = './tests/fixtures/'
FIXTURES_DIR2 = './tests/fixtures/nested/'

# Пути к обычным файлам
path1 = os.path.join(FIXTURES_DIR, 'file1.json')
path2 = os.path.join(FIXTURES_DIR, 'file2.json')

# Пути к файлам с вложенными структурами
nested_path1 = os.path.join(FIXTURES_DIR2, 'nested_file1.json')
nested_path2 = os.path.join(FIXTURES_DIR2, 'nested_file2.json')
nested_path3 = os.path.join(FIXTURES_DIR2, 'nested_file1.yml')
nested_path4 = os.path.join(FIXTURES_DIR2, 'nested_file2.yml')


def generate_diff(file_path1, file_path2):
    # Определяем формат файла по расширению
    file_ext1 = file_path1.split('.')[-1]
    file_ext2 = file_path2.split('.')[-1]

    # Читаем данные из файлов
    with open(file_path1) as file1:
        if file_ext1 == 'json':
            data1 = json.load(file1)
        elif file_ext1 in ['yaml', 'yml']:
            data1 = yaml.safe_load(file1)
        else:
            raise ValueError(f"Unsupported file format: {file_ext1}")

    with open(file_path2) as file2:
        if file_ext2 == 'json':
            data2 = json.load(file2)
        elif file_ext2 in ['yaml', 'yml']:
            data2 = yaml.safe_load(file2)
        else:
            raise ValueError(f"Unsupported file format: {file_ext2}")

    # Сравниваем данные и формируем результат
    def make_diff(data1, data2, parent=""):
        diff = []
        keys = sorted(set(data1.keys()) | set(data2.keys()))
        for key in keys:
            path = f"{parent}.{key}" if parent else key
            if key not in data1:
                diff.append({
                    "key": path,
                    "value": data2[key],
                    "status": "added"
                })
            elif key not in data2:
                diff.append({
                    "key": path,
                    "value": data1[key],
                    "status": "deleted"
                })
            elif data1[key] == data2[key]:
                diff.append({
                    "key": path,
                    "value": data1[key],
                    "status": "unchanged"
                })
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff.extend(make_diff(data1[key], data2[key], path))
            else:
                diff.append({
                    "key": path,
                    "old_value": data1[key],
                    "new_value": data2[key],
                    "status": "updated"
                })
        return diff

    diff = make_diff(data1, data2)

    # вывод
    result = "{\n"
    for item in diff:
        if item["status"] == "added":
            result += "  + {0}: {1}\n".format(item["key"], json.dumps(item["value"], indent=2, ensure_ascii=False))
        elif item["status"] == "deleted":
            result += "  - {0}: {1}\n".format(item["key"], json.dumps(item["value"], indent=2, ensure_ascii=False))
        elif item["status"] == "updated":
            result += "  - {0}: {1}\n".format(item["key"], json.dumps(item["old_value"], indent=2, ensure_ascii=False))
            result += "  + {0}: {1}\n".format(item["key"], json.dumps(item["new_value"], indent=2, ensure_ascii=False))
        else:
            result += "    {0}: {1}\n".format(item["key"], json.dumps(item["value"], indent=2, ensure_ascii=False))
    result += "}"
    return result
