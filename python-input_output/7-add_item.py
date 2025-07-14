#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list stored in a JSON file.
"""

import sys

load_mod = __import__('6-load_from_json_file')
load_from_json_file = load_mod.load_from_json_file

save_mod = __import__('5-save_to_json_file')
save_to_json_file = save_mod.save_to_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)

