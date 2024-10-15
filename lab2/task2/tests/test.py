import memory_profiler
import random
import time
import unittest

from ..scr.main import merge_sort


class TestOverwrite(unittest.TestCase):

    def test_merge_array1(self):

        array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        with open("output.txt", "w") as file:
            file.write("")
            file.close()

        memory_before = memory_profiler.memory_usage()[0]

        tmp = time.time()
        self.assertEqual(merge_sort(array, 0, len(array)), sorted(array))
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

    def test_merge_array100000(self):
        N = 10**5
        array = [random.randint(1, 10**9) for i in range(N)]

        with open("output.txt", "w") as file:
            file.write("")
            file.close()

        memory_before = memory_profiler.memory_usage()[0]

        tmp = time.time()
        self.assertEqual(merge_sort(array, 0, len(array)), sorted(array))
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")


if __name__ == '__main__':
    unittest.main()
