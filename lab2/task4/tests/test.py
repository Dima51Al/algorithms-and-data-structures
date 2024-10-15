import memory_profiler
import random
import time
import unittest

from lab2.task4.src.main import binSearch


class testBinSearch(unittest.TestCase):

    def test_base(self):
        file = open(
            "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task4\\src\\input.txt").readlines()[
            1]
        array = list(map(int, file.split()))

        file = open(
            "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task4\\src\\input.txt").readlines()[
            3]
        values = list(map(int, file.split()))

        memory_before = memory_profiler.memory_usage()[0]

        final_array = [binSearch(array, i) for i in values]

        tmp = time.time()
        self.assertEqual(final_array, [2, 0, -1, 0, -1])
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

    def test_100000(self):
        N = 10**5
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]

        memory_before = memory_profiler.memory_usage()[0]

        final_array = [binSearch(array, i) for i in values]

        tmp = time.time()
        self.assertEqual(final_array, values)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print(N)
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

if __name__ == '__main__':
    unittest.main()
