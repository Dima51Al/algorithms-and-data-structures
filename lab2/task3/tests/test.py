
import unittest
from lab2.utils import *
from lab2.task3.src.main import merge_sort


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

        self.assertEqual(base_test(merge_sort, array, 0, len(array)), 0)


        write_file(str(merge_sort(array, 0, len(array))))

    def test_mergesort_from_array_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(merge_sort, array, 0, len(array)), 499500)

    def test_mergesort_from_array_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(merge_sort, array, 0, len(array)), 49995000)

    def test_mergesort_from_array_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(merge_sort, array, 0, len(array)), 4999950000)


if __name__ == '__main__':
    unittest.main()
