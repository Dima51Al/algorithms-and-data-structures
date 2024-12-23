import os
from bisect import bisect_left


def main(array):
    array_of_values = [-10 ** 9 - 1] + [10 ** 9 + 1] * len(array)

    last_index_for = [-1] * (len(array) + 1)
    preview_index = [-1] * len(array)
    length = 0

    for i in range(len(array)):

        j = bisect_left(array_of_values, array[i], 1)

        if array_of_values[j - 1] < array[i] < array_of_values[j]:
            array_of_values[j] = array[i]
            last_index_for[j] = i
            preview_index[i] = last_index_for[j - 1]
            length = max(length, j)

    answer = []
    p = last_index_for[length]
    while p != -1:
        answer.append(array[p])
        p = preview_index[p]

    return len(answer), answer[::-1]


if __name__ == '__main__':
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    from lab7.utils import read_file_line, write_file, normVid

    array = list(map(int, read_file_line(path_input, 1).split()))

    answer = main(array)

    write_file(path_output, f"{answer[0]}\n{normVid(answer[1])}")
