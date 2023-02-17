#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        'first_file',
        help='path to the first file'
    )

    parser.add_argument(
        'second_file',
        help='path to the second file'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0'
    )

    args = parser.parse_args()


if __name__ == '__main__':
    main()

