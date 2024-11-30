import unittest
from lab3.task5.src.main import h_index
from lab3.utils import *


class HIndexTestCase(unittest.TestCase):

    def test_should_randomize_h_index_min(self):
        # given
        N = 0
        array = random_array(N, -10**8, 10**8)

        # when
        start_memory, start_time = memory_and_time()
        result = h_index(array)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_h_index_avg(self):
        # given
        N = 1000
        array = random_array(N, -10**8, 10**8)

        # when
        start_memory, start_time = memory_and_time()
        result = h_index(array)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_h_index_max(self):
        # given
        N = 5000
        array = random_array(N, -10**8, 10**8)

        # when
        start_memory, start_time = memory_and_time()
        result = h_index(array)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
