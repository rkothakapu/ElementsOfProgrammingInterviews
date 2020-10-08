from typing import List


def plus_one(A: List[int]) -> List[int]:
    """
    [1, 2, 9] -> [1, 3, 0]
    :param A:
    :return:
    """
    B = list(A)
    for i in reversed(range(len(B))):
        B[i] += 1
        if B[i] < 10:
            return B
        elif i == 0:
            return [1] + [0] * len(A)
        else:
            B[i] = 0


def plus_one_book_solution(A: List[int]) -> List[int]:
    """
    Contains example of for else statement
    :param A:
    :return:
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    else:
        if A[0] == 10:
            A[0] = 1
            A.append(0)

    return A


if __name__ == "__main__":
    A = [9, 9, 9]
    print(A, plus_one(A))

    print(A, plus_one_book_solution(A))