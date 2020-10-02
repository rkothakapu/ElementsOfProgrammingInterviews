def count_bits(x: int) -> int:
    """
    Return number of non-zero bits in a nonnegative integer
    :param x: nonnegative integer
    :return: number of non-zero bits
    """
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits