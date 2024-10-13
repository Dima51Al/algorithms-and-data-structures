import memory_profiler
import random
import time
import unittest

from lab2.task1.scr.main import merge_sort


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        N = 10 ** 3
        array = [random.randint(1, 1000) for i in range(N)]


        memory_before = memory_profiler.memory_usage()[0]

        tmp = time.time()
        self.assertEqual(merge_sort(array, 0, N), sorted(array))
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")


if __name__ == '__main__':
    unittest.main()
