
import unittest
from utils import *
from lab2.task3.src.main import merge_sort


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        path = "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task1\\txtf"
        path_input = path + "\\input.txt"
        path_output = path + "\\output.txt"


        file = read_file_line(path_input, 1)

        array = list(map(int, file.split()))

        num = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, num, 0)

        write_file(path_output, str(num))

    def test_merge_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]

        num = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, num, 499500)



    def test_merge_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        num = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, num, 49995000)

    def test_merge_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        num = merge_sort(array, 0, len(array))
        test_base(self.assertEqual, num, 4999950000)


if __name__ == '__main__':
    unittest.main()
