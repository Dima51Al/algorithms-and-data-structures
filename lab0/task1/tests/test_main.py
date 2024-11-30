import unittest

from lab2.utils import *

import lab0.task1.src.tsk1 as tsk1
import lab0.task1.src.tsk2 as tsk2
import lab0.task1.src.tsk3 as tsk3
import lab0.task1.src.tsk4 as tsk4

class FirstTaskCaseTest(unittest.TestCase):

    def test_summ_task_1(self):
        self.assertEqual(base_test(tsk1.summ, 100, 100), 100+100)

    def test_summ_task_2(self):
        self.assertEqual(base_test(tsk2.sum_x_xx, 100, 100), 100+100**2)

    def test_summ_task_3(self):
        array = read_file().split()
        n1, n2 = int(array[0]), int(array[1])
        self.assertEqual(base_test(tsk3.summ, n1, n2), n1 + n2)


    def test_summ_task_4(self):
        array = read_file().split()
        n1, n2 = int(array[0]), int(array[1])
        self.assertEqual(base_test(tsk4.sum_x_xx, n1, n2), n1 + n2**2)


if __name__ == '__main__':
    unittest.main()
