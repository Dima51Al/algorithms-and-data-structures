import memory_profiler
import time
import unittest

from lab2.task3.src.main import merge_sort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        file = open(
            "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task3\\src\\input.txt", "w")
        file.write("10**5\n" + normVid([i for i in range(10 ** 5, 0, -1)]))

        file = open(
            "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task3\\src\\input.txt").readlines()[
            1]
        array = list(map(int, file.split()))

        memory_before = memory_profiler.memory_usage()[0]

        inversion_count = merge_sort(array, 0, len(array))

        tmp = time.time()
        self.assertEqual(inversion_count, (len(array) * (len(array) - 1)) // 2)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

        with open("C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task3\\src\\output.txt",
                  "w") as file:
            file.write(str(inversion_count))

    def test_merge_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]

        memory_before = memory_profiler.memory_usage()[0]

        inversion_count = merge_sort(array, 0, len(array))

        tmp = time.time()
        self.assertEqual(inversion_count, (len(array) * (len(array) - 1)) // 2)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print(N, inversion_count)
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

    def test_merge_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        memory_before = memory_profiler.memory_usage()[0]

        inversion_count = merge_sort(array, 0, len(array))

        tmp = time.time()
        self.assertEqual(inversion_count, (len(array) * (len(array) - 1)) // 2)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print(N, inversion_count)
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")

    def test_merge_100000(self):
        N = 16
        array = [i for i in range(N, 0, -1)]

        memory_before = memory_profiler.memory_usage()[0]

        inversion_count = merge_sort(array, 0, len(array))

        tmp = time.time()
        self.assertEqual(inversion_count, 120)
        tmp = time.time() - tmp

        memory_after = memory_profiler.memory_usage()[0]

        print()
        print(N, inversion_count)
        print("Время выполнения: ", tmp)
        print("Использование памяти: ", memory_after - memory_before, "МБ")


if __name__ == '__main__':
    unittest.main()
