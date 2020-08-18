def returnEvenChars(string):
    result = ""
    for el in range(len(string)):
        if el % 2 == 0:
            result = result + string[el]
    return result

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', help='string')
    args = parser.parse_args()

    print(returnEvenChars(args.string))
