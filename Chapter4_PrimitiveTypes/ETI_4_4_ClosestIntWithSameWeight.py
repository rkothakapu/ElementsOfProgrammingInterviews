def closest_int_with_same_bit_weight(x: int) -> int:
    """
    Define the weight of a non-negative integer x to be the number of bits that are set to 1 in its bin representation.
    Ex: 92 - 1011100 has weight 4
    :param x: non-negative integer
    :return: y such that w(x) = w(y) and |y - x| is small as possible
    """
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits - 1):
        if (x >> i) & 1 != (x >> i+1) & 1:
            x ^= (1 << i) | (1 << (i+1))  # Flip the bits at i, i+1 pos, i.e, swap them
            return x

    raise ValueError("All bits are either '0' or '1")
