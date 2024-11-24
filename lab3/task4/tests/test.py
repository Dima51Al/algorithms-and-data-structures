import unittest
from lab3.utils import *
from lab3.task4.src.main import *

class Dots_and_Segments_TestCase(unittest.TestCase):

    def test_dot_and_segments_from_file(self):
        gwt(
            title="test_dot_and_segments_from_file",
            given="A file containing segment endpoints and dot positions",
            when="The segments and dots are processed to determine coverage",
            then="The output matches the expected result for the example [1, 0, 0]"
        )

        s = int(read_file_line(path_input, 0).split()[0])
        segment_array = []

        for i in range(s):
            x = int(read_file_line(path_input, i+1).split()[0])
            y = int(read_file_line(path_input, i+1).split()[1])
            segment_array.append((x, y))

        dot_array = list(map(int, read_file_line(path_input, s+1).split()))

        self.assertEqual(base_test(main, segment_array, dot_array), [1, 0, 0])

        write_file(normVid(main(segment_array, dot_array)))

    def test_dot_and_segments_max_values(self):
        gwt(
            title="test_dot_and_segments_max_values",
            given="10,000 segments with random large values and 10,000 random dots",
            when="The segments and dots are processed to determine coverage",
            then="The algorithm completes within the expected time of 77-80 seconds"
        )

        s = 10000
        p = 10000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)
        base_test(main, segment_array, dot_array)

    def test_dot_and_segments_avg_values(self):
        gwt(
            title="test_dot_and_segments_avg_values",
            given="5,000 segments with random large values and 5,000 random dots",
            when="The segments and dots are processed to determine coverage",
            then="The algorithm completes within the expected time of 77-80 seconds"
        )

        s = 5000
        p = 5000
        segment_array = [(random.randint(-10**8, 10**8), random.randint(-10**8, 10**8)) for _ in range(s)]
        dot_array = random_array(p, -10**8, 10**8)
        base_test(main, segment_array, dot_array)


if __name__ == '__main__':
    unittest.main()
