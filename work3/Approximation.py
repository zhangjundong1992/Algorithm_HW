def fibonacci(n):
    factor = (1 + 5 ** 0.5) / 2
    return factor ** n / (5 ** 0.5)


for i in range(200):
    print( fibonacci(i))
