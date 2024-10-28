import unittest
from lab1.utils import *
from lab1.task4.src.main import *

class MergeSortTestCase(unittest.TestCase):

    def test_binsearch_from_file(self):
        file_0 = read_file_line(path_input, 0)
        file_1 = read_file_line(path_input, 1)
        array = list(map(int, file_0.split()))
        values = int(file_1)
        self.assertEqual(first=base_test(lineSearch, array, values), second=1)
        write_file(str(lineSearch(array, values)))

    def test_binsearch_from_array_1000(self):
        N = 1000
        array = [i for i in range(0, N)]
        values = 5
        self.assertEqual(first=base_test(lineSearch, array, values), second=5)

    def test_binsearch_from_array_10000(self):
        N = 10000
        array = [i for i in range(0, N)]
        values = 9999
        self.assertEqual(first=base_test(lineSearch, array, values), second=9999)

    def test_binsearch_from_array_100000(self):
        N = 100000
        array = [i for i in range(0, N)]
        values = 99999
        self.assertEqual(first=base_test(lineSearch, array, values), second=99999)


if __name__ == '__main__':
    unittest.main()
