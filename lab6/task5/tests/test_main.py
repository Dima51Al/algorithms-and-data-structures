import random
import unittest
from lab6.task5.src.main import USA
from lab6.utils import *


class USATestCase(unittest.TestCase):

    def test_should_phonebook_add_max_values(self):
        # given
        difficulty = 10**6
        phonebook = USA()


        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            phonebook.add_candidate(str(random.randint(1, 100)), 1)


        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 64)


if __name__ == '__main__':
    unittest.main()
