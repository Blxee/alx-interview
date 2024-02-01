#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): the data to be ckecked.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    length = 0
    for byte in data:
        if length == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                length = 1
            elif byte >> 4 == 0b1110:
                length = 2
            elif byte >> 3 == 0b11110:
                length = 3
            else:
                return False
        elif byte >> 6 == 0b10:
            length -= 1
        else:
            return False
    return (length == 0)
