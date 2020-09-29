from Chapter4_PrimitiveTypes.CTCI import CommonBitTasks


def insertion(N, M, i, j):
    """
    Insert M into N such that M starts at bit j and ends at bit i.
    :param N: 32 bit number
    :param M: 32 bit number
    :param i: bit position start
    :param j: bit position end
    :return: 32 bit number
    """
    while M:
        v = CommonBitTasks.getBit(M, 0)  # Get the left most bit from M
        N = CommonBitTasks.updateBit(N, i, v)  # update a bit in N with M at appropriate pos
        M = M >> 1  # right shift M until 0
        i = i + 1  # update next pos

    return N


if __name__ == "__main__":
    M = 0b10011
    N = 0b10_000_000_000
    i = 2
    j = 6
    print("Input:", bin(N), bin(M), i, j)
    print("Output:", bin(insertion(N, M, i, j)))
