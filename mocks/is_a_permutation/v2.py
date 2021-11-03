#!/bin/env python

def is_perm(a,b):
    if len(a) != len(b):
        return False
    sorted_a = ''.join(sorted(a))
    sorted_b = ''.join(sorted(b))
    if sorted_a == sorted_b:
        return True
    else:
        return False
