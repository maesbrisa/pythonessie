#!/bin/env python
import argparse
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', action='store_true', help='sort by key')
    parser.add_argument('--value', action='store_true', help='sort by value')
    parser.add_argument('--reverse', action='store_true', help='reversed sort')
    parser.add_argument('--dict', required=True, help='dict to sort')
    args = parser.parse_args()
    dictionary = json.loads(args.dict)
    import operator
    index=0 if args.key else 1
    if args.reverse:
        print({k:v for k,v in sorted(dictionary.items(), key=operator.itemgetter(index), reverse=True)})
    else:
        print({k:v for k,v in sorted(dictionary.items(), key=operator.itemgetter(index))})
