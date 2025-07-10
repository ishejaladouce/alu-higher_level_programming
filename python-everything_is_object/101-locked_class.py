#!/usr/bin/python3
"""Defines a LockedClass that restricts dynamic attribute creation."""


class LockedClass:
    """Allows only 'first_name' attribute to be set on instances."""
    __slots__ = ['first_name']
