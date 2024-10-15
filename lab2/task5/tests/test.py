import memory_profiler
import random
import time
import unittest

from lab2.task5.src.main import majority


class testBinSearch(unittest.TestCase):

    def test_base(self):
        path = "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task5\\src\\input.txt"
        file = open(path).readlines()[1]
        array = list(map(int, file.split()))

        memory_before = memory_profiler.memory_usage()[0]

        tmp = time.time()
        self.assertEqual(majority(array), 1)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

    def test_100000(self):
        N = 10 ** 5
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]

        memory_before = memory_profiler.memory_usage()[0]

        tmp = time.time()
        self.assertEqual(majority(array), 0)
        memory_after = memory_profiler.memory_usage()[0]
        tmp = time.time() - tmp



        print()
        print(N)
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")


if __name__ == '__main__':
    unittest.main()
