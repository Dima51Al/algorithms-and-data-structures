# tests.py
import unittest
from lab3.utils import *
from lab3.task1.src.main import *


class QuickSortTestCase(unittest.TestCase):

    def test_randomize_inversion_from_file(self):
        gwt(
            title="test_randomize_inversion_from_file",
            given="A file",
            when="The quicksort algorithm is applied to the list",
            then="The sorted list matches the Python built-in sorted() function"
        )

        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))

        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))

        write_file(normVid(array))


    def test_randomize_aray_1000(self):
        gwt(
            title="test_randomize_inversion_from_file",
            given="An array of 1000 random integers between 1 and 10^9",
            when="The quicksort algorithm is applied to the list",
            then="The sorted list matches the Python built-in sorted() function"
        )

        N = 10 ** 3
        from random import randint
        array = [randint(1, 10**9) for i in range(N)]
        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))

    def test_randomize_aray_10000(self):
        gwt(
            title="test_randomize_aray_10000",
            given="An array of 10,000 random integers between 1 and 10^9",
            when="The randomize_quicksort algorithm is applied to the array",
            then="The sorted array matches the Python built-in sorted() function",
        )
        N = 10 ** 4
        array = [randint(1, 10**9) for i in range(N)]

        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))

    def test_randomize_aray_100000(self):
        gwt(
            title="test_randomize_array_100000",
            given="An array of 100,000 random integers between 1 and 10^9",
            when="The randomize_quicksort algorithm is applied to the array",
            then="The sorted array matches the Python built-in sorted() function",
        )
        N = 10 ** 5
        array = [randint(1, 10**9) for i in range(N)]

        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))


    def test_randomize_inversion_aray_1000(self):
        gwt(
            title="test_randomize_inversion_aray_1000",
            given="An array of 1000 random integers between 1 and 10^9",
            when="The quicksort algorithm is applied to the array",
            then="The sorted array matches the Python built-in sorted() function",
        )
        N = 10 ** 3
        array = [i for i in range(N, -1, -1)]
        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))

    def test_randomize_inversion_aray_10000(self):
        gwt(
            title="test_randomize_inversion_aray_10000",
            given="An array of 10,000 random integers between 1 and 10^9",
            when="The quicksort algorithm is applied to the array",
            then="The sorted array matches the Python built-in sorted() function",
        )
        N = 10 ** 4
        array = [i for i in range(N, -1, -1)]

        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))

    def test_randomize_inversion_aray_100000(self):
        gwt(
            title="test_randomize_inversion_aray_100000",
            given="An array of 100,000 random integers between 1 and 10^9",
            when="The quicksort algorithm is applied to the array",
            then="The sorted array matches the Python built-in sorted() function",
        )
        N = 10 ** 5
        array = [i for i in range(N, -1, -1)]

        base_test(randomize_quicksort, array, 0, len(array))
        self.assertEqual(array, sorted(array))


if __name__ == '__main__':
    unittest.main()
