import random


def quick_sort(lst, left, right):
    if left >= right:
        return

    rd = random.randint(left, right)
    lst[left], lst[rd] = lst[rd], lst[left]

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
