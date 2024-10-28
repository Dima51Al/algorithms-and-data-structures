import unittest
from lab1.utils import *
from lab1.task6.src.main import *

class SelectionSortTestCase(unittest.TestCase):

    def test_Bubble_sort_from_file(self):
        file = read_file_line(path_input, 0)

        array = list(map(int, file.split()))

        self.assertEqual(base_test(Bubble_sort, array), sorted(array))

        write_file(normVid(Bubble_sort(array)))

    def test_Bubble_sort_from_array_1000(self):
        N = 1000
        array = [i for i in range(N, 0, -1)]
        self.assertEqual(base_test(Bubble_sort, array), sorted(array))

    def test_Bubble_sort_from_array_10000(self):
        N = 10000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(Bubble_sort, array), sorted(array))

    def test_Bubble_sort_from_array_100000(self):
        N = 100000
        array = [i for i in range(N, 0, -1)]

        self.assertEqual(base_test(Bubble_sort, array), sorted(array))


if __name__ == '__main__':
    unittest.main()

