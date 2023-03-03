import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='path to file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')  # по умолчанию используем форматер "stylish"
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.filepath) as file:
        data = json.load(file)
    result = format(data, args.format)  # передаем форматер, указанный в аргументах
    print(result)


if __name__ == '__main__':
    main()
