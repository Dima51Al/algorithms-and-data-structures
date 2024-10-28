import unittest

from lab2.utils import *

from lab0.task2.src.tsk import *



class FirstTaskCaseTest(unittest.TestCase):

    def test_file_fib(self):
        noun = int(read_file())
        self.assertEqual(base_test(fib, noun), 55)
        write_file(str(fib(noun)))


    def test_fib(self):
        self.assertEqual(base_test(fib, 10), 55)
        self.assertEqual(base_test(fib, 1), 1)
        self.assertEqual(base_test(fib, -100), -1)



if __name__ == '__main__':
    unittest.main()
