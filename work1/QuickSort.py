import numpy as np


def quick_sort(lst, left, right):
    if left >= right:
        return
    i = left
    j = right
    axis = lst[i]

    while i < j:
        while i < j and lst[j] >= axis:
            j -= 1
        lst[i] = lst[j]
        while i < j and lst[i] <= axis:
            i += 1
        lst[j] = lst[i]
    lst[i] = axis
    quick_sort(lst, left, i - 1)
    quick_sort(lst, i + 1, right)


# m_lst = [2, 6, 18, 7, 9, 10, 5, 12, 15, work3]
# quick_sort(m_lst, 0, len(m_lst) - 1)
# print("the result of quick sort is")
# print(m_lst)
lst = np.arange(998)
# np.random.shuffle(lst)
quick_sort(lst,0,len(lst)-1)
print(lst)
