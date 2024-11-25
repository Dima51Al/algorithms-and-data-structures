import unittest
from lab3.task3.src.main import *


class PugaloTestCase(unittest.TestCase):

    def test_should_pugalo_1000(self):
        # given
        N = 10 ** 3
        array = random_array(N, 0, 10)
        arm_len = 3

        # when
        start_memory, start_time = memory_and_time()
        self.assertEqual(pugalo(array, arm_len), False)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_pugalo_10000(self):
        # given
        N = 10 ** 4
        array = random_array(N, 0, 10)
        arm_len = 3

        # when
        start_memory, start_time = memory_and_time()
        pugalo(array, arm_len)
        self.assertEqual(pugalo(array, arm_len), False)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_pugalo_100000(self):
        # given
        N = 10 ** 5
        array = random_array(N, 0, 10)
        arm_len = 3

        # when
        start_memory, start_time = memory_and_time()
        pugalo(array, arm_len)
        self.assertEqual(pugalo(array, arm_len), False)
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
