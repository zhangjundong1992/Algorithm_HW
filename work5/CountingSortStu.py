import numpy as np


def counting_sort(A, k):
    n = len(A)
    B = A[:]
    C = list(np.zeros(k, int))

    for j in range(n):
        C[A[j].rem] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j].rem] - 1] = A[j]
        C[A[j].rem] -= 1

    return B
