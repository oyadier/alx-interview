#!/usr/bin/python3
"""UTF-8 Character encoding"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding.
        Args:
            data (integer): an integer character
        Return:
            True if it a valid utf code else false
    """
    mask_one = 1 << 7
    mask_two = 1 << 6
    number_bytes = 0

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_one and not (i & mask_two)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
