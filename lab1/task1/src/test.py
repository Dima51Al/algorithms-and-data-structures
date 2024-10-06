import random
import time
from main import insertionSort
from memory_profiler import memory_usage

import psutil

def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s



# array = [random.randint(-10 ** 9, 10 ** 9) for i in range(N)]
array = [0]
# array = [31, 41, 59, 26, 41, 58]
tmp = time.time()
N = len(array)
string = f"{N}" + "\n" + normVid(array)
open("input.txt", "w").write(string)
import psutil
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
insertionSort()
print(time.time() - tmp, "seconds")

