import unittest
from lab4.task6.src.main import take_from_queue_with_min, put_to_queue_with_min, init_queue_with_min, min_from_queue
from lab4.utils import *


class QueueTestCase(unittest.TestCase):

    def test_should_randomize_dot_and_segments_max_values(self):
        # given
        difficulty = 10**6
        # when
        start_memory, start_time = memory_and_time()

        queue_array = init_queue_with_min()
        for i in range(difficulty):
            put_to_queue_with_min(queue_array, 10**9)
        for i in range(difficulty):
            take_from_queue_with_min(queue_array)
            min_from_queue(queue_array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
