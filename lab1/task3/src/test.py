import random
import time

import psutil

from main import insertionSort, normVid

array = [random.randint(-10**9, 10**9) for i in range(10**3)]

print("len array:", len(array))
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("../txtf/input.txt", "w").write(string)
tmp = time.time()
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")
print()



array = [0]
print("len array:", len(array))
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("../txtf/input.txt", "w").write(string)
tmp = time.time()
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")