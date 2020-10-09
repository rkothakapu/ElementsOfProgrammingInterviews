from typing import List


def can_reach_end(A: List[int]) -> bool:
    """
    :param A: Represent the board game. The ith entry in A is the maximum we can advance from i
    :return:whether it is possible to advance to the last index starting from the begining of the array
    """
    max_reach = A[0]
    i = 1
    while len(A) - 1 > max_reach >= i:
        max_reach = max(max_reach, i + A[i])
        i += 1

    return max_reach >= len(A) - 1