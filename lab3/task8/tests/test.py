import unittest
from lab3.utils import *
from lab3.task8.src.main import *

class Dots_TestCase(unittest.TestCase):

    def test_dot_from_file(self):
        s = int(read_file_line(path_input, 0).split()[0])
        k = int(read_file_line(path_input, 0).split()[1])
        segment_array = []

        for i in range(s):
            x = int(read_file_line(path_input, i+1).split()[0])
            y = int(read_file_line(path_input, i+1).split()[1])
            segment_array.append([x, y])

        self.assertEqual(base_test(main, segment_array, k), [[-2, 2]])

        write_file(normVid(main(segment_array, k)))


    def test_dot_and_segments_max_values(self):
        n = 100000
        k = n
        segment_array = [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(n)]
        base_test(main, segment_array, k)
        """0.35 сек"""