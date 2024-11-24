import unittest
from lab3.task5.src.main import h_index
from lab3.utils import *


class HIndexTestCase(unittest.TestCase):

    def test_h_index_from_file(self):
        gwt(
            title="test_h_index_from_file",
            given="A file containing a list of integers representing citation counts",
            when="The h-index algorithm is applied to the array",
            then="The computed h-index matches the expected result (3 for the example)"
        )

        str_arr = read_file_line(path_input, 0).split()
        array = list(map(int, str_arr))
        self.assertEqual(base_test(h_index, array), 3)
        write_file(str(h_index(array)))

    def test_h_index_min(self):
        gwt(
            title="test_h_index_min",
            given="An empty array of citation counts",
            when="The h-index algorithm is applied",
            then="The algorithm handles the edge case without errors"
        )

        N = 0
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)

    def test_h_index_avg(self):
        gwt(
            title="test_h_index_avg",
            given="An array of 1,000 random integers representing citation counts",
            when="The h-index algorithm is applied to the array",
            then="The algorithm completes successfully and returns a valid h-index"
        )

        N = 1000
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)

    def test_h_index_max(self):
        gwt(
            title="test_h_index_max",
            given="An array of 5,000 random integers representing citation counts",
            when="The h-index algorithm is applied to the array",
            then="The algorithm completes successfully within the expected time (77-80 seconds)"
        )

        N = 5000
        array = random_array(N, -10**8, 10**8)
        base_test(h_index, array)
        """77-80 секунд"""


if __name__ == '__main__':
    unittest.TestCase()
