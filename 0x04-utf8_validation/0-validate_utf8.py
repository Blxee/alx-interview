#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): the data to be ckecked.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    if len(data) == 0:
        return False
    try:
        bytes(data).decode()
        return True
    except:
        return False
