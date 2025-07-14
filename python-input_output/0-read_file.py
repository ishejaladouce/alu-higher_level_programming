#!/usr/bin/python3
"""
Module that reads a UTF-8 text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
