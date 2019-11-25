def merge_sort(lst, left, right):
    if right - left <= 0:
        return
    mid = int((right + left) / 2)
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)
    merge(lst, left, mid, right)


def merge(lst, left, mid, right):
    i = left
    j = mid + 1
    while i < j:
        while i < mid and lst[i] <= lst[j]:
            i += 1
        if lst[i] <= lst[j]:
            return
        while j < right and lst[j] <= lst[i]:
            j += 1
        if lst[j] <= lst[i]:
            reverse(lst, i, mid)
            reverse(lst, mid + 1, j)
            reverse(lst, i, j)
            return
        reverse(lst, i, mid)
        reverse(lst, mid + 1, j - 1)
        reverse(lst, i, j - 1)
        i += j - mid - 1
        mid = j - 1


def reverse(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
