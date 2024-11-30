import random
import unittest
from lab4.task8.src.main import postfix
from lab4.utils import *


class PostfixTestCase(unittest.TestCase):

    def test_should_postfix(self):
        # given
        difficulty = 10**6
        input_array = []
        for i in range(difficulty):
            input_array.append("5")
        for i in range(difficulty-1):
            input_array.append("+")


        # when
        start_memory, start_time = memory_and_time()

        postfix(input_array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
