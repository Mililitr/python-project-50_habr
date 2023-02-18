#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first file to compare')
    parser.add_argument('second_file', help='second file to compare')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    if args.format:
        print(f'Comparing files: {args.first_file} vs {args.second_file} using format: {args.format}')
    else:
        print(f'Comparing files: {args.first_file} vs {args.second_file}')

if __name__ == '__main__':
    main()

