#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    ma_sk_1 = 1 << 7
    ma_sk_2 = 1 << 6

    for x in data:

        ma_sk_byte = 1 << 7

        if number_bytes == 0:

            while ma_sk_byte & x:
                number_bytes += 1
                ma_sk_byte = ma_sk_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (x & ma_sk_1 and not (x & ma_sk_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
