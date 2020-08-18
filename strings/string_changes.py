#!/bin/env python

def returnChangedString(string):
    sample = string[1:]
    changes = sample.replace(string[0], '$')
    return string[0]+changes


if __name__ == '__main__':
    lista_examples = ['alpinista', 'ordenador', 'router', 'movil']
    for a in lista_examples:
        print(returnChangedString(a))
