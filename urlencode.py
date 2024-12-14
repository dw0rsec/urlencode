#!/usr/bin/env python3

import urllib.parse
import argparse
import sys

def url_encode(string):
    if not string:
        print('error: the following arguments are required: STRING')
        sys.exit(1)

    encoded_string = urllib.parse.quote(string)
    encoded_string = encoded_string.strip()

    return encoded_string

def url_decode(string):
    if not string:
        print('error: the following arguments are required: STRING')

    decoded_string = urllib.parse.unquote(string)

    return decoded_string

def main():
    parser = argparse.ArgumentParser(description='A tool to URL encode and decode strings')
    parser.add_argument('-e', '--encode', action='store_true', help='url encode a string')
    parser.add_argument('-d', '--decode', action='store_true', help='url decode a string')
    parser.add_argument('STRING', nargs='?', help='the string to process')

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    string = args.STRING

    if args.encode:
        print(url_encode(string))

    if args.decode:
        print(url_decode(string))

if __name__ == '__main__':
    main()
