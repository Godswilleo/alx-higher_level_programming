#!/usr/bin/python3
""" demonstrates returning an object from a json string """
import json


def from_json_string(my_str):
    """ demonstrates the returning an object from a json string """
    return json.loads(my_str)
