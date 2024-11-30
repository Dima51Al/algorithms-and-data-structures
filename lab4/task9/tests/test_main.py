import unittest
from lab4.utils import *
from lab4.task9.src.main import Queue


class QueueCenterTestCase(unittest.TestCase):

    def test_should_check_max_size(self):
        # given
        difficulty = 10**6
        input_array = [0]*difficulty
        for i in range(difficulty):
            input_array[i] = 10**9

        # when
        start_memory, start_time = memory_and_time()

        result = Queue(input_array).get_array()

        final_memory, final_time = memory_and_time()


        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


    def test_should_max_requests(self):
        # given
        difficulty = 10**5
        input_array = Queue([0])


        # when
        start_memory, start_time = memory_and_time()



        for i in range(difficulty):
            input_array.center_push(10**9)

        for i in range(difficulty):
            input_array.dequeue()

        result = input_array.get_array()


        final_memory, final_time = memory_and_time()



        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_queue_get_array(self):
        # given
        queue1 = Queue([])
        queue2 = Queue([1])
        queue3 = Queue([1, 2])
        queue4 = Queue([1, "2", 3])
        queue5 = Queue([1, "2", 3, 4])
        queue6 = Queue([1, "2", [3, 4]])

        # when
        start_memory, start_time = memory_and_time()

        result1 = queue1.get_array()
        result2 = queue2.get_array()
        result3 = queue3.get_array()
        result4 = queue4.get_array()
        result5 = queue5.get_array()
        result6 = queue6.get_array()

        final_memory, final_time = memory_and_time()

        # then
        self.assertEqual(result1, [])
        self.assertEqual(result2, [1])
        self.assertEqual(result3, [1, 2])
        self.assertEqual(result4, [1, "2", 3])
        self.assertEqual(result5, [1, "2", 3, 4])
        self.assertEqual(result6, [1, "2", [3, 4]])

        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)

    def test_should_enqueue_dequeue(self):
        # given
        queue1 = Queue([])
        queue2 = Queue([1])
        queue3 = Queue([1, 2])
        queue4 = Queue([1, "2", 3])
        queue5 = Queue([1, "2", 3, 4])
        queue6 = Queue([1, "2", [3, 4]])

        # when
        queue1.enqueue("123")
        queue2.enqueue("123")
        queue3.enqueue("123")

        result1 = queue1.get_array()
        result2 = queue2.get_array()
        result3 = queue3.get_array()

        queue4.dequeue()
        queue5.dequeue()
        queue6.dequeue()
        result4 = queue4.get_array()
        result5 = queue5.get_array()
        result6 = queue6.get_array()

        # then
        self.assertEqual(result1, ["123"])
        self.assertEqual(result2, [1, "123"])
        self.assertEqual(result3, [1, 2, "123"])
        self.assertEqual(result4, ["2", 3])
        self.assertEqual(result5, ["2", 3, 4])
        self.assertEqual(result6, ["2", [3, 4]])


if __name__ == '__main__':
    unittest.main()
