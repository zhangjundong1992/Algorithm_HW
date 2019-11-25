from work4 import MergeOri as mo
from work4 import MergeInPlace as mip
from work4 import RandomizedQuickSort as rqs
import numpy as np
import time

lst1 = list(np.random.randint(0, 100000, 10000))
lst2 = lst1.copy()
lst3 = lst1.copy()

start = time.time()
mo.merge_sort(lst1)
end = time.time()
print("merge sort:", end="")
print(end - start)

start = time.time()
mip.merge_sort(lst2, 0, len(lst2) - 1)
end = time.time()
print("merge_in_place:", end="")
print(end - start)

start = time.time()
rqs.quick_sort(lst3, 0, len(lst3) - 1)
end = time.time()
print("quick sort:", end="")
print(end - start)
