# tests.py
import unittest
from lab3.utils import *
from lab3.task3.src.main import *


class QuickSortTestCase(unittest.TestCase):

    def test_pugalo_from_file(self):
        gwt(
            title="test_pugalo_from_file",
            given="A file containing an array of integers and a scarecrow arm length",
            when="The scarecrow algorithm is applied to the array",
            then="The result matches the expected outcome written to the file ('ДА' or 'НЕТ')"
        )

        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))

        arm_len = int(read_file_line(path_input, 0).split()[1])

        self.assertEqual(base_test(pugalo, array, arm_len), True)

        if pugalo(array, arm_len):
            write_file("ДА")
        else:
            write_file("НЕТ")

    def test_random_aray_1000(self):
        gwt(
            title="test_random_aray_1000",
            given="An array of 1,000 random integers between 0 and 10 and a scarecrow arm length of 3",
            when="The scarecrow algorithm is applied to the array",
            then="The algorithm's result matches the expected output"
        )

        N = 10 ** 3
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)

    def test_random_aray_10000(self):
        gwt(
            title="test_random_aray_10000",
            given="An array of 10,000 random integers between 0 and 10 and a scarecrow arm length of 3",
            when="The scarecrow algorithm is applied to the array",
            then="The algorithm's result matches the expected output"
        )

        N = 10 ** 4
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)

    def test_random_aray_100000(self):
        gwt(
            title="test_random_aray_100000",
            given="An array of 100,000 random integers between 0 and 10 and a scarecrow arm length of 3",
            when="The scarecrow algorithm is applied to the array",
            then="The algorithm's result matches the expected output"
        )

        N = 10 ** 5
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)


if __name__ == '__main__':
    unittest.main()
