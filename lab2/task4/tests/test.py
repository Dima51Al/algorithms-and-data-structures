import unittest
from utils import *
from lab2.task4.src.main import *


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_binsearch_from_file(self):
        file_0 = read_file_line(path_input, 1)
        file_1 = read_file_line(path_input, 3)
        array = list(map(int, file_0.split()))
        values = list(map(int, file_1.split()))

        self.assertEqual(first=base_test(array_bin_search, array, values), second=[2, 0, -1, 0, -1])

        write_file( normVid(array_bin_search(array, values)))

    def test_binsearch_from_array_1000(self):
        N = 1000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        self.assertEqual(first=base_test(array_bin_search, array, values), second=[i for i in range(0, N, 20)])

        

    def test_binsearch_from_array_10000(self):
        N = 10000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        self.assertEqual(first=base_test(array_bin_search, array, values), second=[i for i in range(0, N, 20)])


    def test_binsearch_from_array_100000(self):
        N = 100000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        self.assertEqual(first=base_test(array_bin_search, array, values), second=[i for i in range(0, N, 20)])


if __name__ == '__main__':
    unittest.main()
