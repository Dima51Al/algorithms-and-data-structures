import random
import time
from main import insertionSort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


s = open("input.txt").readlines()[1]
array = [int(x) for x in s.split()]

tmp = time.time()
array = [random.randint(-10**9, 10**9) for i in range(10**3)]
tmp = time.time()
string = "1000"+"\n" + normVid(array)
open("input.txt", "w").write(string)
insertionSort()

print(time.time() - tmp, "seconds")
