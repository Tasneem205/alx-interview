#!/usr/bin/python3
""" UTF-8 validation file """


def validUTF8(data):
    """ validate using utf-8 """
    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        if num > 255:
            return False
        if num_bytes == 0:
            if num & mask1 == 0:
                continue
            elif num & mask1 and num & mask2:
                mask = 1 << 7
                while num & mask:
                    num_bytes += 1
                    mask >>= 1

                if num_bytes == 1 or num_bytes > 4:
                    return False
            else:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
