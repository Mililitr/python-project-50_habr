import json

def format_diff_as_json(diff):
    """Возвращает JSON-строку с отформатированным результатом сравнения.
    Args:
        diff: результат сравнения в виде словаря.
    Returns:
        Отформатированный результат сравнения в виде JSON-строки.
    """
    return json.dumps(diff, indent=2, ensure_ascii=False)
