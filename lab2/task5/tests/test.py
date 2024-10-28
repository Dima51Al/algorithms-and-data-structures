import unittest
from lab2.utils import *
from lab2.task5.src.main import *





class MergeSortTestCase(unittest.TestCase):

    def test_majority_from_file(self):
        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))
        self.assertEqual(first=base_test(majority, array), second=1)
        write_file(str(majority(array)))

    def test_majority_from_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(first=base_test(majority, array), second=0)


    def test_majority_from_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(first=base_test(majority, array), second=0)

    def test_majority_from_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(first=base_test(majority, array), second=0)


if __name__ == '__main__':
    unittest.main()
