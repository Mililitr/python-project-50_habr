import argparse
from gendiff.generat_diff import generate_diff
from gendiff.formatters import stylish, plain, as_json


def main():
    parser = argparse.ArgumentParser(description='Generate diff', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('filepath1', type=str, help='path to first file')
    parser.add_argument('filepath2', type=str, help='path to second file')
    parser.add_argument('-f', '--format', type=str, default='stylish', choices=['stylish', 'plain', 'json'],
                        help='output format (default: stylish)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0', help='show program\'s version number and exit')
    args = parser.parse_args()

    diff = generate_diff(args.filepath1, args.filepath2, args.format)

    if args.format == 'stylish':
        print(stylish.format_diff_as_stylish(diff))
    elif args.format == 'plain':
        print(plain.format_diff_as_plain(diff))
    elif args.format == 'json':
        print(as_json.format_diff_as_json(diff))
    else:
        raise ValueError(f'Unknown format: {args.format}')


if __name__ == '__main__':
    main()
