import unittest
from lab3.task7.src.main import main, main_with_index
from lab3.utils import *


class RadixSortTestCase(unittest.TestCase):
    def test_radix_sort_file(self):
        def vertical_to_horizontal(vertical_data):
            rows = len(vertical_data)
            cols = len(vertical_data[0])
            horizontal_data = [''.join(vertical_data[row][col] for row in range(rows)) for col in range(cols)]
            return horizontal_data

        gwt(
            title="test_radix_sort_file",
            given="A file containing a number of strings to be sorted lexicographically",
            when="The radix sort algorithm is applied to the input data",
            then="The output matches the expected sorted list"
        )

        n = read_file_line(path_input, 0)
        n = n.split()
        n = n[0]
        n = int(n)

        input_data = []


        for i in range(1, n + 1):
            input_data.append(read_file_line(path_input, i).replace("\n", "").replace(" ", ""))
        input_data_tmp = vertical_to_horizontal(input_data)
        input_data = []
        for i in range(len(input_data_tmp)):
            input_data.append((input_data_tmp[i], i+1))


        expected_output = [2, 3, 1]
        self.assertEqual(base_test(main_with_index, input_data, 0), expected_output)
        write_file(normVid(expected_output))

    def test_radix_sort_simple(self):
        gwt(
            title="test_radix_sort_simple",
            given="A small list of strings ['bab', 'bba', 'baa']",
            when="The radix sort algorithm is applied",
            then="The output is ['baa', 'bab', 'bba']"
        )

        input_data = ["bab", "bba", "baa"]
        expected_output = ["baa", "bab", "bba"]
        self.assertEqual(base_test(main, input_data), expected_output)

    def test_radix_sort_empty(self):
        gwt(
            title="test_radix_sort_empty",
            given="An empty list of strings",
            when="The radix sort algorithm is applied",
            then="The output is an empty list"
        )

        input_data = []
        expected_output = []
        self.assertEqual(base_test(main, input_data), expected_output)

    def test_radix_sort_single_element(self):
        gwt(
            title="test_radix_sort_single_element",
            given="A list with a single string ['abc']",
            when="The radix sort algorithm is applied",
            then="The output matches the input"
        )

        input_data = ["abc"]
        expected_output = ["abc"]
        self.assertEqual(base_test(main, input_data), expected_output)

    def test_radix_sort_identical_elements(self):
        gwt(
            title="test_radix_sort_identical_elements",
            given="A list with identical strings ['aaa', 'aaa', 'aaa']",
            when="The radix sort algorithm is applied",
            then="The output matches the input"
        )

        input_data = ["aaa", "aaa", "aaa"]
        expected_output = ["aaa", "aaa", "aaa"]
        self.assertEqual(base_test(main, input_data), expected_output)

    def test_radix_sort_random(self):
        gwt(
            title="test_radix_sort_random",
            given="A random list of strings ['acd', 'zab', 'baa', 'bab', 'bbb']",
            when="The radix sort algorithm is applied",
            then="The output is the sorted list ['acd', 'baa', 'bab', 'bbb', 'zab']"
        )

        input_data = ["acd", "zab", "baa", "bab", "bbb"]
        expected_output = ["acd", "baa", "bab", "bbb", "zab"]
        self.assertEqual(base_test(main, input_data), expected_output)

    def test_radix_sort_max(self):
        gwt(
            title="test_radix_sort_max",
            given="A large list of 1,000,000 random strings sampled from ['acd', 'zab', 'baa', 'bab', 'bbb']",
            when="The radix sort algorithm is applied",
            then="The algorithm completes successfully"
        )

        input_data_0 = ["acd", "zab", "baa", "bab", "bbb"]
        input_data = [input_data_0[random.randint(0, 4)] for i in range(10**6)]

        base_test(main, input_data)


if __name__ == '__main__':
    unittest.main()
