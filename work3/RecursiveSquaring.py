import numpy as np


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = np.array([
        [1, 1],
        [1, 0]
    ])

    b = np.linalg.matrix_power(a, n - 1)
    return b[0][0]


for i in range(10):
    print(fibonacci(i))
