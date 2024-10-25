import random
import time
import psutil
from main import selectionSort, normVid




array = [random.randint(-10 ** 9, 10 ** 9) for i in range(10**3)]
print("len array:", len(array))
N = len(array)
string = normVid(array) + "\n" + f"{N}"
open("../txtf/input.txt", "w").write(string)
tmp = time.time()
selectionSort()
print(time.time() - tmp)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
print()


array = [0]
print("len array:", len(array))
N = len(array)
string = normVid(array) + "\n" + f"{N}"
open("../txtf/input.txt", "w").write(string)
tmp = time.time()
selectionSort()
print(time.time() - tmp)
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
print()