import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate diff',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )
    return parser.parse_args()
