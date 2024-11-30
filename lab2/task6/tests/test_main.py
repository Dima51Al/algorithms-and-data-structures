
import unittest
from lab2.task6.src.main import *


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


class MergeSortTestCase(unittest.TestCase):

    def test_file_input(self):

        array = []
        for i in open(path_input, "r", encoding="utf-8").readlines():
            array.append([i.split()[0], float(i.split()[1].replace(",", "."))])

        write_file(max_delta(array))

        self.assertEqual(base_test(max_delta, array), "купить 16.07.1980 продать 16.03.1981 получить 55.400000000000006")


if __name__ == '__main__':
    unittest.main()
