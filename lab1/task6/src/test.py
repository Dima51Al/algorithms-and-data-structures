import random
import time

import psutil

from main import Bubble_sort, normVid


array = [0]
# array = [random.randint(-10 ** 9, 10 ** 9) for i in range(10**3)]
array = [i for i in range(10**3, 0, -1)]
# array = [5, 4, 3, 2, 1]
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("input.txt", "w").write(string)

tmp = time.time()
""" """
Bubble_sort()
""" """
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
print(time.time()-tmp)


