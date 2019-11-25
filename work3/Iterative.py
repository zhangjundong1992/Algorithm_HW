def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    lst = [0 for j in range(n + 1)]
    lst[0] = 0
    lst[1] = 1

    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]

    return lst[-1]


for i in range(200):
    print(fibonacci(i))
