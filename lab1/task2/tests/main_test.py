import unittest
from lab1.utils import *
from lab1.task2.src.main import insertionSort


class MergeSortTestCase(unittest.TestCase):

    def test_mergesort_from_file(self):
        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))

        self.assertEqual(base_test(insertionSort, array), [[-1, 1, 3, 1, 2, 4], [26, 31, 41, 41, 58, 59]])

    def test_mergesort_from_array_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(insertionSort, array), [[1 for _ in range(N)], [i + 1 for i in range(N)]])

    def test_mergesort_from_array_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(insertionSort, array), [[1 for _ in range(N)], [i + 1 for i in range(N)]])


    def test_mergesort_from_array_100000(self):
            N = 100000
            array = [i for i in range(N, 0, -1)]
            self.assertEqual(base_test(insertionSort, array), [[1 for _ in range(N)], [i + 1 for i in range(N)]])


if __name__ == '__main__':
    unittest.main()
