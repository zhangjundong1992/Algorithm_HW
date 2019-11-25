import numpy as np


def counting_sort(A, k):
    n = len(A)
    B = list(np.zeros(n, int))
    C = list(np.zeros(k, int))

    for j in range(n):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B


lst = list(np.random.randint(0, 1000, 100))
print(counting_sort(lst, 1001))
