import unittest
from lab3.utils import *
from lab3.task8.src.main import *

class Dots_TestCase(unittest.TestCase):

    def test_dot_from_file(self):
        gwt(
            title="test_dot_from_file",
            given="A file containing segments and a target number of dots (k)",
            when="The main algorithm is applied to find the minimum set of dots that cover all segments",
            then="The output matches the expected result [[-2, 2]] for the example input"
        )

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
        gwt(
            title="test_dot_and_segments_max_values",
            given="A maximum input of 100,000 segments with random endpoints and k equal to the number of segments",
            when="The main algorithm is applied",
            then="The algorithm completes within 0.35 seconds without errors"
        )

        n = 10**5
        k = n
        segment_array = [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(n)]
        base_test(main, segment_array, k)
        """0.35 сек"""


if __name__ == '__main__':
    unittest.main()
