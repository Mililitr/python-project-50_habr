from gendiff.formatters.stylish import format_diff_as_stylish
from gendiff.formatters.plain import format_diff_as_plain
from gendiff.formatters.as_json import format_diff_as_json

FORMATTERS = {
    'stylish': format_diff_as_stylish,
    'plain': format_diff_as_plain,
    'json': format_diff_as_json,
}

def generate_diff(file1, file2, format_name):
    # Здесь реализуйте функцию generate_diff
    diff = {}  # Предполагаемый результат функции generate_diff
    formatter = FORMATTERS.get(format_name)
    if formatter:
        return formatter(diff)
    else:
        raise ValueError(f'Unknown format: {format_name}')
