from typing import List


def bool_sort(A: List[int]) -> None:
    """
    Given an Array of n objects with Boolean values keys, reorder the array so that objects that have the False key
    appear first. The relative ordering o objects with key True should not change.
    :param A: List of integers. 0 -> False, non-0: True
    :return: None
    """
    # Keep the following invariants during partitioning:
    # zero: Right-most zero to swap the next non zero in our right to left pass
    zero = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] == 0:
            continue
        else:
            A[i], A[zero] = A[zero], A[i]
            zero -= 1


if __name__ == "__main__":
    A = [1, 0, 2, 0, 0, 3, 0, 4, 0, 0, 0, 5]
    bool_sort(A)
    print(A)