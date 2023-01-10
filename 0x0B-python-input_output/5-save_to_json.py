#!/usr/bin/python3
""" write object to file using json representation """

import json

def save_to_json_file(my_obj, filename):
    """ function to write json represenation to text file """
    with open(filename, mode="w", encoding="utf-8") as f:
    jsonObject = json.dumps(my_obj)
    f.write(jsonObject)
