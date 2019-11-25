lst = [2, 6, 18, 7, 9, 10, 5, 12, 15, 3]
n = len(lst)

# bubble sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 注意交换变量的方法

print("the result of bubble sort is")
print(lst)
