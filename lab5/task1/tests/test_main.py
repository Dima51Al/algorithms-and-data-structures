import unittest
from lab5.task1.src.main import is_heap
from lab5.utils import memory_and_time, random_array


class IsHeapTestCase(unittest.TestCase):


    def test_should_is_heap_false(self):
        # given
        array = [1, 0, 1, 2, 0]
        # when
        start_memory, start_time = memory_and_time()

        result = is_heap(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertFalse(result)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


    def test_should_is_heap_true(self):
        # given
        array = [1, 3, 2, 5, 4]
        # when
        start_memory, start_time = memory_and_time()

        result = is_heap(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertTrue(result)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


    def test_should_is_heap_max_values(self):
        # given
        difficulty = 10**6
        array = random_array(difficulty, -2*10**9, 2*10**9)
        # when
        start_memory, start_time = memory_and_time()

        result = is_heap(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
