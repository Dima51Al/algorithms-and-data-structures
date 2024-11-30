import os
import unittest
from lab3.utils import *
from lab3.task4.src.main import *

class DotsAndSegmentsTestCase(unittest.TestCase):

    def test_should_randomize_dots_and_segments_max_values(self):
        # given
        s = 1000
        p = 10000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)

        # when
        start_memory, start_time = memory_and_time()
        main(segment_array, dot_array)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_dots_and_segments_avg_values(self):
        # given
        s = 5000
        p = 5000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)

        # when
        start_memory, start_time = memory_and_time()
        main(segment_array, dot_array)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
