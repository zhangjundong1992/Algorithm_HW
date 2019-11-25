lst = [2, 6, 18, 7, 9, 10, 5, 12, 15, 3]
n = len(lst)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("the result of select sort is")
print(lst)
