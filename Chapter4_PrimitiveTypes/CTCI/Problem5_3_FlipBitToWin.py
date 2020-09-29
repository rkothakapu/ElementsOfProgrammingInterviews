from Chapter4_PrimitiveTypes.CTCI.CommonBitTasks import getBit


def flipBitToWin(num):
    """
    You can flip exactly one bit from a 0 to 1.
    Find the length of the longest sequence of 1s you could create
    :param num: int
    :return: int
    """
    if ~num == 0:
        return len(bin(num))

    currentLength = 0
    previousLength = 0
    maxLength = 1

    while num != 0:
        if (num & 1) == 1:
            currentLength += 1
        else:
            previousLength = 0 if num & 2 == 0 else currentLength
            currentLength = 0
        maxLength = max(previousLength + currentLength + 1, maxLength)
        num = (num % 0x100000000) >> 1
    return maxLength


if __name__ == "__main__":
    print(1775, bin(1775), flipBitToWin(1775))
    print(-10, bin(-10), flipBitToWin(-10))