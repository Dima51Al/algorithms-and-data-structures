import unittest
from lab4.utils import *
from lab4.task13part1.src.main import Stack


class StackTestCase(unittest.TestCase):

    def test_should_check_max_size(self):
        # given
        difficulty = 10**6
        input_array = [0]*difficulty
        for i in range(difficulty):
            input_array[i] = 10**9


        # when
        start_memory, start_time = memory_and_time()



        result = Stack(input_array).get_array()


        final_memory, final_time = memory_and_time()



        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


    def test_should_stack_get_array(self):
        # given
        array1 = Stack([])
        array2 = Stack([1])
        array3 = Stack([1, 2])
        array4 = Stack([1, "2", 3])
        array5 = Stack([1, "2", 3, 4])
        array6 = Stack([1, "2", [3, 4]])

        # when
        start_memory, start_time = memory_and_time()

        result1 = array1.get_array()
        result2 = array2.get_array()
        result3 = array3.get_array()
        result4 = array4.get_array()
        result5 = array5.get_array()
        result6 = array6.get_array()


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


    def test_should_push_pop(self):
        # given
        array1 = Stack([])
        array2 = Stack([1])
        array3 = Stack([1, 2])
        array4 = Stack([1, "2", 3])
        array5 = Stack([1, "2", 3, 4])
        array6 = Stack([1, "2", [3, 4]])

        # when


        array1.push("123")
        array2.push("123")
        array3.push("123")

        result1 = array1.get_array()
        result2 = array2.get_array()
        result3 = array3.get_array()

        array4.pop()
        array5.pop()
        array6.pop()
        result4 = array4.get_array()
        result5 = array5.get_array()
        result6 = array6.get_array()




        # then
        self.assertEqual(result1, ["123"])
        self.assertEqual(result2, [1, "123"])
        self.assertEqual(result3, [1, 2, "123"])
        self.assertEqual(result4, [1, "2"])
        self.assertEqual(result5, [1, "2", 3])
        self.assertEqual(result6, [1, "2"])


if __name__ == '__main__':
    unittest.main()
