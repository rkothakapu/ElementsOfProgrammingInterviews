def swap_bits(x: int, i: int, j: int) -> int:
    """
    :param x: number in which bits are to be swapped
    :param i: position i
    :param j: position j
    :return: number after bits at loc i, j are swapped
    """
    # hint: When is the swap necessary?
    # Swap is necessary if bits at i, j are different, i.e. bit_i ^ bit_j = 1
    if x & (1 << i) ^ x & (1 << j):
        x ^= (1 << i) | (1 << j)
    return x
