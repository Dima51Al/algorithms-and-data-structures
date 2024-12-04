import random
import unittest
from lab5.task3.src.main import main
from lab5.utils import memory_and_time


class QueueTestCase(unittest.TestCase):

    def test_should_queue_ex_1(self):
        # given
        array = []
        buffer = 1
        # when
        start_memory, start_time = memory_and_time()

        result = main(array, buffer)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, None)
        self.assertLessEqual(final_time - start_time, 10)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_queue_ex_2(self):
        # given
        array = [[0, 0]]
        buffer = 1
        # when
        start_memory, start_time = memory_and_time()

        result = main(array, buffer)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, [0])
        self.assertLessEqual(final_time - start_time, 10)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_queue_ex_3(self):
        # given
        array = [[0, 1], [0, 1]]
        buffer = 1
        # when
        start_memory, start_time = memory_and_time()

        result = main(array, buffer)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, [0, -1])
        self.assertLessEqual(final_time - start_time, 10)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_queue_ex_14(self):
        # given
        array = [[i, 2] for i in range(6)]
        buffer = 3
        # when
        start_memory, start_time = memory_and_time()

        result = main(array, buffer)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, [0, 2, 4, 6, 8, -1])
        self.assertLessEqual(final_time - start_time, 10)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_queue_max_values(self):
        # given


        n = 10**5
        buffer = 10**5

        array = [[random.randint(1, 10**6), random.randint(0, 10**3)] for _ in range(n)]

        # when
        start_memory, start_time = memory_and_time()

        result = main(array, buffer)

        final_memory, final_time = memory_and_time()

        # then

        self.assertLessEqual(final_time - start_time, 10)
        self.assertLessEqual(final_memory - start_memory, 512)


if __name__ == '__main__':
    unittest.main()
