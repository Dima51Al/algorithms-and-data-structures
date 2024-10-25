import random
import time

import psutil

from main import insertionSort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


s = open("../txtf/input.txt").readlines()[1]
array = [int(x) for x in s.split()]
print("len array:", len(array))
N = len(array)
tmp = time.time()
string = f"{N}"+"\n" + normVid(array)
open("../txtf/input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")
print()

array = [random.randint(-10**9, 10**9) for i in range(10**3)]
print("len array:", len(array))
N = len(array)
tmp = time.time()
string = f"{N}"+"\n" + normVid(array)
open("../txtf/input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")
print()


array = [31, 41, 59, 26, 41, 58]
print("len array:", len(array))
N = len(array)
tmp = time.time()
string = f"{N}"+"\n" + normVid(array)
open("../txtf/input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")



