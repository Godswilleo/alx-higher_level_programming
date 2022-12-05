#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence != '':
        first = sentence[0]
        length = len(sentence)
    else:
        first = None

    return(length, first)
