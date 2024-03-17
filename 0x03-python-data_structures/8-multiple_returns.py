#!/usr/bin/python3

def multiple_returns(sentence):
    slen = len(sentence)
    if slen > 0:
        return (slen, sentence[0])
    return (0, None)
