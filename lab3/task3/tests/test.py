# tests.py
import unittest
from lab3.utils import *
from lab3.task3.src.main import *


class QuickSortTestCase(unittest.TestCase):


    def test_pugalo_from_file(self):
        file = read_file_line(path_input, 1)
        array = list(map(int, file.split()))

        arm_len = int(read_file_line(path_input, 0).split()[1])


        self.assertEqual(base_test(pugalo, array, arm_len), True)

        if pugalo(array, arm_len):
            write_file("ДА")
        else:
            write_file("НЕТ")

    def test_random_aray_1000(self):
        N = 10 ** 3
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)

    def test_random_aray_10000(self):
        N = 10 ** 4
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)

    def test_random_aray_100000(self):
        N = 10 ** 5
        array = random_array(N, 0, 10)
        arm_len = 3
        self.assertEqual(base_test(pugalo, array, arm_len), False)



if __name__ == '__main__':
    unittest.main()
