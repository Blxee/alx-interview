#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): the data to be ckecked.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    skip
    for i, byte in enumerate(data):
        if not (0 <= byte <= 255):
            return False
        if i == 0:
            if not (
                byte & 0b1 == 0b0
                or byte & 0b111 == 0b110
                or byte & 0b1111 == 0b1110
                or byte & 0b11111 == 0b11110
            ):
                return False
    return True
