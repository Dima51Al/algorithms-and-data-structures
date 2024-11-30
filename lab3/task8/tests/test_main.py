import unittest
from lab3.task8.src.main import *
from lab3.utils import *


class DotsTestCase(unittest.TestCase):

    def test_should_randomize_dot_and_segments_max_values(self):
        # given
        n = 10**5
        k = n
        segment_array = [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(n)]

        # when
        start_memory, start_time = memory_and_time()
        result = main(segment_array, k)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
