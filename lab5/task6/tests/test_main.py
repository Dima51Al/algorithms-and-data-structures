import unittest
from lab5.task6.src.main import main, QueueModified
from lab5.utils import memory_and_time, random_array


class QueueModifiedTestCase(unittest.TestCase):


    def test_should_main_enqueue(self):
        # given
        difficulty = 10**6

        array = QueueModified()
        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            array.enqueue(10**6 - i)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_main_D(self):
        # given
        array = QueueModified([1, 2, 3, 4])
        difficulty = 10**6
        # when
        start_memory, start_time = memory_and_time()


        for i in range(difficulty):
            array.D(1, 10**9)

        result = array.get_array()

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_main_min(self):
        # given
        difficulty = 10 ** 6
        array = QueueModified([])
        array.enqueue()
        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            array.get_min()

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
