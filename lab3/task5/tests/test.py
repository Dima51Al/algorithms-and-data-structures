import unittest
from lab3.task5.src.main import h_index
from lab3.utils import *


class HIndexTestCase(unittest.TestCase):

    def test_h_index_from_file(self):


        str_arr = read_file_line(path_input, 0).split()
        array = list(map(int, str_arr))
        self.assertEqual(base_test(h_index, array), 3)
        write_file(str(h_index(array)))

    def test_h_index_min(self):


        N = 0
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)

    def test_h_index_avg(self):


        N = 1000
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)

    def test_h_index_max(self):

        N = 5000
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)
        """77-80 секунд"""


if __name__ == '__main__':
    unittest.TestCase()
