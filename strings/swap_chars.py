def return_string(s1,s2):
    s1_1 = s2[:2]+s1[2:]
    s2_1 = s1[:2]+s2[2:]
    return s1_1 + ' ' + s2_1


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--string1', help='First string to swap')
    parser.add_argument('--string2', help='second')
    args = parser.parse_args()

    print(return_string(args.string1, args.string2))
