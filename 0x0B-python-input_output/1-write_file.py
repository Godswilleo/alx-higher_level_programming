#!/usr/bin/python3
""" module demonstrates writing to txt files """


def write_file(filename="", text=""):
    """ function demonstrates writing to a txt file """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
