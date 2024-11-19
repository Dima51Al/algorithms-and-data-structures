# tests.py
import unittest
from lab3.task7.src.main import main
from lab3.utils import *


class RadixSortTestCase(unittest.TestCase):
    def test_radix_sort_file(self):


        n = read_file_line(path_input, 0)
        n = n.split()
        n = n[0]
        n = int(n)

        input_data = []
        for i in range(1, n + 1):
            input_data.append(read_file_line(path_input, i).replace("\n", "").replace(" ", ""))

        expected_output = ["baa", "bab", "bba"]
        self.assertEqual(main(input_data), expected_output)



    def test_radix_sort_simple(self):

        input_data = ["bab", "bba", "baa"]
        expected_output = ["baa", "bab", "bba"]
        self.assertEqual(main(input_data), expected_output)

    def test_radix_sort_empty(self):

        input_data = []
        expected_output = []
        self.assertEqual(main(input_data), expected_output)

    def test_radix_sort_single_element(self):

        input_data = ["abc"]
        expected_output = ["abc"]
        self.assertEqual(main(input_data), expected_output)

    def test_radix_sort_identical_elements(self):

        input_data = ["aaa", "aaa", "aaa"]
        expected_output = ["aaa", "aaa", "aaa"]
        self.assertEqual(main(input_data), expected_output)

    def test_radix_sort_random(self):
        input_data = ["acd", "zab", "baa", "bab", "bbb"]
        expected_output = ["acd", "baa", "bab", "bbb", "zab"]
        self.assertEqual(main(input_data), expected_output)




if __name__ == '__main__':
    unittest.main()
