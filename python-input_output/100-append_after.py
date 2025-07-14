#!/usr/bin/python3
"""
Module that defines a function to insert a line after
each line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_string after each line containing search_string in filename.

    Args:
        filename (str): The path to the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after matching lines.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
