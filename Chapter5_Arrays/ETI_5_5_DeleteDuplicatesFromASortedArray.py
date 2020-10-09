from typing import List


def delete_duplicates(A: List[int]) -> int:
    """
    Program which takes as input a sorted array and updates it so that all duplicates have been removed and the
    remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements.

    :param A: sorted Array may contain duplicates
    :return: number of unique elements
    """
    num_unique = 1 if len(A) > 0 else 0
    for i in range(1, len(A)):
        if A[i] != A[num_unique - 1]:
            A[num_unique], A[i] = A[i], A[num_unique]
            num_unique += 1
    return num_unique


if __name__ == "__main__":
    A = [0, 0, 1, 2, 2, 2, 3, 5, 5]
    print(delete_duplicates(A), A)
