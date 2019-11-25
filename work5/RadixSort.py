import math
from work5.Excel import *
from work5.CountingSortStu import *


def radix_sort(lst_stu, upper):
    # 计算基数排序的轮数，注意向上取整保证比较完所有的数字
    n = len(lst_stu)
    d = math.ceil(math.log(upper, n))

    # 构造用于技术排序的数组，
    lst_radix = []
    for i in range(n):
        lst_radix.append(ele_radix(lst_stu[i], lst_stu[i].tel, 0))

    # 进行d轮计数排序
    for j in range(d):
        for k in range(n):
            lst_radix[k].rem = lst_radix[k].val % n
            lst_radix[k].val = int(lst_radix[k].val / n)

        lst_radix = counting_sort(lst_radix, n)

    # 将排序结果赋值回原数组
    for m in range(n):
        lst_stu[m] = lst_radix[m].stu


lst = get_xls()
radix_sort(lst, 20000000000)
for i in range(len(lst)):
    print(lst[i].name + " : " + str(lst[i].tel))
