import unittest
from lab6.task6.src.main import HashSet
from lab6.utils import *


class USATestCase(unittest.TestCase):

    def test_should_fib_add_max_values(self):
        # given
        difficulty = 2*10**5
        phonebook = HashSet()


        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            phonebook.is_in(10**180-1)


        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 128)

    def test_should_fib_true(self):
        # given
        difficulty = [1, 2, 144, 89, 55]
        phonebook = HashSet()
        result = True

        # when
        start_memory, start_time = memory_and_time()

        for i in difficulty:
            result = result and phonebook.is_in(i)


        final_memory, final_time = memory_and_time()

        # then
        self.assertTrue(result)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 128)


    def test_should_fib_false(self):
        # given
        difficulty = [4, 32, 143, 88, 54]
        phonebook = HashSet()
        result = True

        # when
        start_memory, start_time = memory_and_time()

        for i in difficulty:
            result = result and phonebook.is_in(i)


        final_memory, final_time = memory_and_time()

        # then
        self.assertFalse(result)
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 128)


if __name__ == '__main__':
    unittest.main()
