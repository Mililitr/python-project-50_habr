import argparse
from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import format_diff_as_stylish
from gendiff.formatters.plain import format_diff_as_plain
from gendiff.formatters.as_json import format_diff_as_json

FORMATTERS = {
    'stylish': format_diff_as_stylish,
    'plain': format_diff_as_plain,
    'json': format_diff_as_json,
}


def format_diff(diff, format_name):
    if format_name in FORMATTERS:
        formatter = FORMATTERS[format_name]
        return formatter(diff)
    else:
        raise ValueError(f'Unknown format: {format_name}')


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=FORMATTERS.keys(),
        default='stylish'
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(format_diff(diff, args.format))


if __name__ == '__main__':
    main()
