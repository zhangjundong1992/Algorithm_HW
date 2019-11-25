import numpy as np


def counting_sort(A, k):
    n = len(A)
    B = list(np.zeros(n, int))
    C = list(np.zeros(k, int))

    for j in range(n):
        C[A[j]] += 1

    # 从后往前，统计小于等于没个取值的个数
    for i in range(k - 2, -1, -1):
        C[i] += C[i + 1]

    for j in range(n):
        B[-C[A[j]]] = A[j]  # ！！！用负号
        C[A[j]] -= 1

    return B


lst = list(np.random.randint(0, 1000, 100))
print(counting_sort(lst, 1001))
