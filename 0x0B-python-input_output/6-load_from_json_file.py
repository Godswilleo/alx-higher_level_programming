#!/usr/bin/python3
""" read from json """
import json

def load_from_json_file(filename):
    """ function to read from json """
    with open(filename, "w", encoding="utf-8") as f:
        return json.loads(f)
