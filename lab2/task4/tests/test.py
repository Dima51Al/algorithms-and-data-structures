import unittest
from utils import *
from lab2.task4.src.main import binSearch


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        path = "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task4\\txtf"
        path_input = path + "\\input.txt"
        path_output = path + "\\output.txt"


        file_0 = read_file_line(path_input, 1)
        file_1 = read_file_line(path_input, 3)
        array = list(map(int, file_0.split()))
        values = list(map(int, file_1.split()))
        sorted_array = [binSearch(array, i) for i in values]

        base_test(self.assertEqual, sorted_array, [2, 0, -1, 0, -1])
        write_file(path_output, normVid(sorted_array))

    def test_merge_1000(self):
        N = 1000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        sorted_array = [binSearch(array, i) for i in values]
        base_test(self.assertEqual, sorted_array, [i for i in range(0, N, 20)])


    def test_merge_10000(self):
        N = 10000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        sorted_array = [binSearch(array, i) for i in values]
        base_test(self.assertEqual, sorted_array, [i for i in range(0, N, 20)])

    def test_merge_100000(self):
        N = 100000
        array = [i for i in range(0, N)]
        values = [i for i in range(0, N, 20)]
        sorted_array = [binSearch(array, i) for i in values]
        base_test(self.assertEqual, sorted_array, [i for i in range(0, N, 20)])


if  __name__ == '__main__':
    unittest.main()
