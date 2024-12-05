import unittest
from lab6.task8.src.main import main
from lab6.utils import *


class USATestCase(unittest.TestCase):

    def test_should_fib_add_max_values(self):
        # given
        N = 10**6
        X = 10**15
        A = 10**3
        B = 10**5
        AC = 16
        BC = 10
        AD = 10**3//2
        BD = 10**15



        # when
        start_memory, start_time = memory_and_time()

        result = main(N, X, A, B, AC, BC, AD, BD)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 5)
        self.assertLessEqual(final_memory - start_memory, 256)



if __name__ == '__main__':
    unittest.main()
