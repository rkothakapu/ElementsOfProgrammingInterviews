def conversion(A, B):
    """
    Write a function to determine the number of bits you would need to flip to convert integer A to integer B
    :param A:
    :param B:
    :return:
    """
    diff = 0
    while A or B:
        if (A & 1) != (B & 1):
            diff += 1
        A >>= 1
        B >>= 1

    return diff


def conversion_book_solution1(A, B):
    count = 0
    c = A ^ B  # all 1 bits in c indicate difference bits between A, B
    while c:
        count += c & 1
        (c % 0x100000000) >> 1
    return count


def conversion_book_solution2(A, B):
    count = 0
    c = A ^ B  # all 1 bits in c indicate difference bits between A, B
    while c:
        count += c & 1
        c = c & (c-1)
    return count


if __name__ == "__main__":
    print(29, bin(29), 15, bin(15), conversion(29, 15))
    print(29, bin(29), 2, bin(2), conversion(29, 2))