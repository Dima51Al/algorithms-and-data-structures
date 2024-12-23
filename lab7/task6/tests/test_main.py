import random
import unittest
from lab7.task6.src.main import main
from lab7.utils import memory_and_time


class IntersectionTestCase(unittest.TestCase):

    def test_should_main_max_len(self):
        # given
        difficulty = 3 * 10 ** 5
        array = [random.randint(-10 ** 9, 10 ** 9) for i in range(difficulty)]

        # when
        start_memory, start_time = memory_and_time()

        result = main(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_main_max_len_with_reverse_array(self):
        # given
        difficulty = 3 * 10 ** 5
        array = [difficulty - i for i in range(difficulty)]

        # when
        start_memory, start_time = memory_and_time()

        result = main(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_main_max_len_with_nonreverse_array(self):
        # given
        difficulty = 3 * 10 ** 5
        array = [i + 1 for i in range(difficulty)]

        # when
        start_memory, start_time = memory_and_time()

        result = main(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
