def getBit(num, i):
    return int((num & (1 << i)) != 0)


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    return num & ~(1 << i)


def clearBitsMSBThroughI(num, i):
    """
    To clear all bits from the most significant bit through i (inclusive)
    Leaves just the last i bits
    :param num:
    :param i:
    :return:
    """
    return num & ((1 << i) - 1)


def clearBitsIThrough0(num, i):
    return num & (-1 << (i+1))


def updateBit(num, i, v):
    v = 1 if v else 0
    return (num & ~(1 << i)) | (v << i)


if __name__ == "__main__":
    print('getBit', "{0:b}".format(25), 3, getBit(25, 3))
    print('setBit', "{0:b}".format(25), 2, "{0:b}".format(setBit(25, 2)))
    print('clearBit', "{0:b}".format(25), 3, "{0:b}".format(clearBit(25, 3)))
    print('clearBitsMSBThroughI', "{0:b}".format(27), 3, "{0:b}".format(clearBitsMSBThroughI(27, 3)))
    print('clearBitsIThrough0', "{0:b}".format(27), 3, "{0:b}".format(clearBitsIThrough0(27, 3)))