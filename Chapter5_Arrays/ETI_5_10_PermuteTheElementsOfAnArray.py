from typing import List


def apply_permutation(perm: List[int], A: List[int]) -> None:
    t = [False] * len(A)
    for i, j in enumerate(perm):
        if not t[i]:
            t[j] = True
            A[i], A[j] = A[j], A[i]


if __name__ == '__main__':
    perm = [2, 0, 1, 3]
    A = ['a', 'b', 'c', 'd']
    apply_permutation(perm, A)
    print(A)
