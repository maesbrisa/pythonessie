def remove_char(string, index):
    return string[:index]+string[index+1:]

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--string', help='string')
    p.add_argument('--index', type=int, help='index')
    args = p.parse_args()
    print(remove_char(args.string, args.index))
