import random
import time
from main import insertionSort
array = [random.randint(-10**9, 10**9) for i in range(10**3)]
tmp = time.time()



insertionSort()
print(time.time() - tmp, "seconds")