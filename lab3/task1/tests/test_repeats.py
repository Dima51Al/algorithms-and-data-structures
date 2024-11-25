import unittest
from lab3.utils import random_array, memory_and_time
from lab3.task1.src.main_repetitions import randomize_quicksort


class QuickSortTestCase(unittest.TestCase):

    def test_should_randomize_quicksort_1000(self):
        # given
        N = 10 ** 3
        array = random_array(N, 1, 10 ** 9)

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_quicksort_10000(self):
        # given
        N = 10 ** 4
        array = random_array(N, 1, 10 ** 9)

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_quicksort_100000(self):
        # given
        N = 10 ** 5
        array = random_array(N, 1, 10 ** 9)

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_quicksort_inversion_1000(self):
        # given
        N = 10 ** 3
        array = [i for i in range(N, -1, -1)]

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_quicksort_inversion_10000(self):
        # given
        N = 10 ** 4
        array = [i for i in range(N, -1, -1)]

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_randomize_quicksort_inversion_100000(self):
        # given
        N = 10 ** 5
        array = [i for i in range(N, -1, -1)]

        # when
        start_memory, start_time = memory_and_time()
        randomize_quicksort(array, 0, len(array)-1)
        self.assertEqual(array, sorted(array))
        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
