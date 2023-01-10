#!/usr/bin/python3
""" Module to demonstrate reading form a txt file"""


def read_file(filename=""):
    """ Function demonstrating reading from a txt file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
