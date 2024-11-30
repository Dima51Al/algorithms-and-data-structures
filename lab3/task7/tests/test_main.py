import os
import unittest
from lab3.task7.src.main import main, main_with_index
from lab3.utils import *

class RadixSortTestCase(unittest.TestCase):

    def test_should_radix_sort_simple(self):
        # given
        input_data = ["bab", "bba", "baa"]
        expected_output = ["baa", "bab", "bba"]

        # when
        start_memory, start_time = memory_and_time()
        result = main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_radix_sort_empty(self):
        # given
        input_data = []
        expected_output = []

        # when
        start_memory, start_time = memory_and_time()
        result = main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_radix_sort_single_element(self):
        # given
        input_data = ["abc"]
        expected_output = ["abc"]

        # when
        start_memory, start_time = memory_and_time()
        result = main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_radix_sort_identical_elements(self):
        # given
        input_data = ["aaa", "aaa", "aaa"]
        expected_output = ["aaa", "aaa", "aaa"]

        # when
        start_memory, start_time = memory_and_time()
        result = main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_radix_sort_random(self):
        # given
        input_data = ["acd", "zab", "baa", "bab", "bbb"]
        expected_output = ["acd", "baa", "bab", "bbb", "zab"]

        # when
        start_memory, start_time = memory_and_time()
        result = main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_radix_sort_max(self):
        # given
        input_data_0 = ["acd", "zab", "baa", "bab", "bbb"]
        input_data = [input_data_0[random.randint(0, 4)] for i in range(10**6)]

        # when
        start_memory, start_time = memory_and_time()
        main(input_data)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()

