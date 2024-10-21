import unittest
from utils import *
from lab2.task2.src.main import merge_sort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        path = "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task2\\txtf"
        path_input = path + "\\input.txt"
        path_output = path + "\\output.txt"


        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))
        sorted_array = merge_sort(array, 0, len(array))

        test_base(self.assertEqual, sorted_array, sorted(array))
        write_file(path_output, normVid(sorted_array))

    def test_merge_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        sorted_array = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, sorted_array, sorted(array))


    def test_merge_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        sorted_array = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, sorted_array, sorted(array))

    def test_merge_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        sorted_array = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, sorted_array, sorted(array))


if __name__ == '__main__':
    unittest.main()
