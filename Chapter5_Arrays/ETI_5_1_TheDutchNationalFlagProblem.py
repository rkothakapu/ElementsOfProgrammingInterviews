from typing import List


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller: equal]
    # unclassified group: A[equal: larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)-1
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        elif A[equal] > pivot:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
        else:
            equal += 1