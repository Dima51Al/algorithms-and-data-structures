
import unittest
from utils import *
from lab2.task6.src.main import *


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_merge(self):
        path = "C:\\Users\\User\\PycharmProjects\\algorithms-and-data-structures\\lab2\\task6\\txtf"
        path_input = path + "\\input.txt"
        path_output = path + "\\output.txt"

        array = []
        for i in open(path_input, "r", encoding="utf-8").readlines():
            array.append([i.split()[0], float(i.split()[1].replace(",", "."))])
        write_file(path_output, max_delta(array))


if __name__ == '__main__':
    unittest.main()
