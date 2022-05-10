def solution(start, length):
    step = length
    end = start + length ** 2
    res = 0
    while start < end:
        min = start
        max = start + length - 1
        start += step
        length -= 1
        if min != max:
            res ^= xor_range(min,max)
        else:
            res ^= min
    return res

def xor_to(n):
    modulus = n & 3  # n % 4

    if modulus == 0:
        return n

    if modulus == 1:
        return 1

    if modulus == 2:
        return n + 1

    return 0


def xor_range(a, b):
    """
    Return the XOR of numbers from A to B.
    """
    return xor_to(b) ^ xor_to(a - 1)
