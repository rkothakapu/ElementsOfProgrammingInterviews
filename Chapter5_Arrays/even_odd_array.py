from typing import List


def even_odd(A: List[int]) -> None:
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 0:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1


if __name__ == "__main__":
    A = [2, 1, 3, 4, 5, 9, 11, 12, 10, 8]
    even_odd(A)
    print(A)