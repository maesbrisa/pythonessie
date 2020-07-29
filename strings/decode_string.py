#!/bin/env python



def damelastring(coded_string, template):
    dictionary = {}
    for char in coded_string:
        if char not in dictionary:
            dictionary.update({char:coded_string.count(char)})

    for i, el in enumerate(reversed(sorted(dictionary))):
        dictionary[el] = template[i]

    for coded_char, decoded_char in dictionary.items():
        coded_string = coded_string.replace(coded_char, decoded_char)
    return coded_string



if __name__ == "__main__":
    import time
    import argparse
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--coded_string', '-c', required=True, help='Give me some string to decode')
    parser.add_argument('--template', '-t', required=True, help='Give me a template to start')
    parser.add_argument('--timeit', action='store_true', help='Just tell me how much time it takes')

    args = parser.parse_args()

    print(damelastring(args.coded_string, args.template))
    end_time = time.time()
    if args.timeit:
        print('Execution time > ' + str(end_time-start_time) + ' seconds' )
