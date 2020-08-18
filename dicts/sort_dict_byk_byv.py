#!/bin/env python
import argparse
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', action='store_true', help='sort by key')
    parser.add_argument('--value', action='store_true', help='sort by value')
    parser.add_argument('--dict', required=True, help='dict to sort')
    args = parser.parse_args()
    dictionary = json.loads(args.dict)

    if args.key:
        print({k:v for k,v in sorted(dictionary.items(), key=lambda item: item[0])})
    else:
        print({k:v for k,v in sorted(dictionary.items(), key=lambda item: item[1])})
