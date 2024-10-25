import random
import unittest


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s

class SortTestCase(unittest.TestCase):

    def testCheckInsertionSort(self):
        array = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
        array = [31, 41, 59, 26, 41, 58]

    def testCheckInsertionSort(self):
        array = [0]

    def testCheckInsertionSort(self):
        array = [random.randint(-10 ** 9, 10 ** 9) for i in range(10 ** 3)]
