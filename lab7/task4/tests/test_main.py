import random
import unittest
from lab7.task4.src.main import intersection
from lab7.utils import memory_and_time


class IntersectionTestCase(unittest.TestCase):

    def test_should_intersection_max_values(self):
        # given

        first_array = [random.randint(-10**9, 10**9) for i in range(100)]
        second_array = [random.randint(-10**9, 10**9) for i in range(100)]

        # when
        start_memory, start_time = memory_and_time()

        result = intersection(first_array, second_array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 1)
        self.assertLessEqual(final_memory - start_memory, 64)

    def test_should_intersection(self):
        # given

        first_array = [1, 2, 3, 4]
        second_array = [2, 3, 4]

        # when
        start_memory, start_time = memory_and_time()

        result = intersection(first_array, second_array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, 3)
        self.assertLessEqual(final_time - start_time, 1)
        self.assertLessEqual(final_memory - start_memory, 64)


if __name__ == '__main__':
    unittest.main()
