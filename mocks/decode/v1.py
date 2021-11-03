#!/bin/env python
import string

def decode(string, guide) -> str:
    decoded = []
    for el in string:
        if not el.isalpha():
            decoded.append(el)
        else:
            decoded.append(guide[el])
    return ''.join(decoded)


if __name__ == '__main__':
    abc = list(string.ascii_lowercase)
    map = ['p','x','m','s','a','c','z','e','v','g','i','j','d','k','n','f','o','r','l','h','t','u','w','b','y','q']
    guide = dict(zip(abc, map))
    print(decode('this works!', guide))
