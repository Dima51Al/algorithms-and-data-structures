import unittest
from lab6.task1.src.main import HashSet
from lab6.utils import *


class PostfixTestCase(unittest.TestCase):

    def test_should_check_hash_add_max_values(self):
        # given
        difficulty = 5*10**5
        hash_set = HashSet()




        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            hash_set.add(10**18-i)


        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_check_hash_remove_max_values(self):
        # given
        difficulty = 5 * 10 ** 5
        hash_set = HashSet()

        for i in range(difficulty):
            hash_set.add(10 ** 18 - i)

        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            hash_set.remove(10 ** 18 - i)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_check_hash_is_in_max_values(self):
        # given
        difficulty = 5 * 10 ** 5
        hash_set = HashSet()
        for i in range(difficulty):
            hash_set.add(10 ** 18 - i)

        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            hash_set.is_in(10 ** 18 - i)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
