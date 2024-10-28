import unittest
from lab2.utils import *
from lab2.task1.src.main import merge_sort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):

        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))
        sorted_array = merge_sort(array, 0, len(array))

        self.assertEqual(base_test(merge_sort, array, 0, len(array)), sorted(array))

        write_file(normVid(sorted_array))

    def test_merge_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(merge_sort, array, 0, len(array)), sorted(array))

    def test_merge_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(merge_sort, array, 0, len(array)), sorted(array))

    def test_merge_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(merge_sort, array, 0, len(array)), sorted(array))


if __name__ == '__main__':
    unittest.main()
