import time
from main import insertionSort

s = open("input.txt").readlines()[1]
array = [int(x) for x in s.split()]

tmp = time.time()

insertionSort()

print(time.time() - tmp, "seconds")