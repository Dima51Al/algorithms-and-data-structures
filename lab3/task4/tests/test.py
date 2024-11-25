import os
import unittest
from lab3.utils import *
from lab3.task4.src.main import *

class Dots_and_Segments_TestCase(unittest.TestCase):

    def test_dot_and_segments_from_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        path_input = os.path.join(parent_dir, 'txtf\\input.txt')
        path_output = os.path.join(parent_dir, 'txtf\\output.txt')

        s = int(read_file_line(path_input, 0).split()[0])
        segment_array = []

        for i in range(s):
            x = int(read_file_line(path_input, i+1).split()[0])
            y = int(read_file_line(path_input, i+1).split()[1])
            segment_array.append((x, y))

        dot_array = list(map(int, read_file_line(path_input, s+1).split()))

        self.assertEqual(base_test(main, segment_array, dot_array), [1, 0, 0])

        write_file(path_output, normVid(main(segment_array, dot_array)))

    def test_dot_and_segments_max_values(self):


        s = 10000
        p = 10000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)
        base_test(main, segment_array, dot_array)

    def test_dot_and_segments_avg_values(self):

        s = 5000
        p = 5000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)
        base_test(main, segment_array, dot_array)


if __name__ == '__main__':
    unittest.main()
