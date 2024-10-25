import unittest
from utils import *
from lab1.task3.src.main import insertionSort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_mergesort_from_file(self):
        file = read_file_line(path_input, 1)

        array = list(map(int, file.split()))

        self.assertEqual(base_test(insertionSort, array), sorted(array, reverse=True))

        write_file(str(insertionSort(array)))

    def test_mergesort_from_array_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(insertionSort, array), sorted(array, reverse=True))

    def test_mergesort_from_array_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(insertionSort, array), sorted(array, reverse=True))

    def test_mergesort_from_array_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(insertionSort, array), sorted(array, reverse=True))


if __name__ == '__main__':
    unittest.main()
