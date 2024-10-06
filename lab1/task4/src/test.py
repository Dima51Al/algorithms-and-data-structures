import random
import time

import psutil

from main import lineSearch


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s



tmp = time.time()
# array = [random.randint(-10 ** 3, 10 ** 3) for i in range(10 ** 3)]
array = [0]
tmp = time.time()
N = len(array)
string = normVid(array) + "\n" + f"{N}"

open("input.txt", "w").write(string)


print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
lineSearch()
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

print(time.time() - tmp, "seconds")
