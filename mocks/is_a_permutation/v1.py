#!/bin/env python


def is_perm(a, b):
    if len(a) != len(b):
        return False
    stack = list(b)
    for el in a:
        try:
            stack.pop(stack.index(el))
        except:
            return False
    return True

