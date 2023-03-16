import json


def format_diff_as_json(diff):
    """Трансформирует diff в формат JSON."""
    # Используем json.dumps для преобразования diff в JSON-строку с отступами в 2 пробела
    json_string = json.dumps(diff, indent=2, separators=(',', ': '))

    # Возвращаем полученную JSON-строку
    return json_string
