import unittest
from lab5.task2.src.main import main
from lab5.utils import memory_and_time


class TreeTestCase(unittest.TestCase):


    def test_should_tree(self):
        # given
        array = [4, -1, 4, 1, 1]
        # when
        start_memory, start_time = memory_and_time()

        result = main(array)

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result, 3)
        self.assertLessEqual(final_time - start_time, 3)
        self.assertLessEqual(final_memory - start_memory, 512)


    def test_should_tree_max_value(self):
        # given
        difficulty = 10**6
        array = [i + 1 for i in range(difficulty)]
        array[-1] = -1
        # when
        start_memory, start_time = memory_and_time()

        result = main(array)

        final_memory, final_time = memory_and_time()

        # then

        self.assertLessEqual(final_time - start_time, 3)
        self.assertLessEqual(final_memory - start_memory, 512)


if __name__ == '__main__':
    unittest.main()
