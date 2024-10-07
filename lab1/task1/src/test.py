import random
import time
import psutil
from main import insertionSort
from memory_profiler import memory_usage

import psutil

def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s



array = [random.randint(-10 ** 9, 10 ** 9) for i in range(10**3)]



print("len array:", len(array))
tmp = time.time()
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")
print()


array = [0]
print("len array:", len(array))
tmp = time.time()
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")
print()


array = [31, 41, 59, 26, 41, 58]
print("len array:", len(array))
tmp = time.time()
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("input.txt", "w").write(string)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")

