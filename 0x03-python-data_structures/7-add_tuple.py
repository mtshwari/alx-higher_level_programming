#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ta = resolve(tuple_a)
    tb = resolve(tuple_b)
    return (ta[0] + tb[0], ta[1] + tb[1])


def resolve(t=()):
    tlen = len(t)
    if tlen == 0:
        tnew = 0, 0
    elif tlen == 1:
        tnew = t[0], 0
    else:
        tnew = t[0], t[1]
    return tnew
