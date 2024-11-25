# сортировка пугалом
import os

from lab3.utils import *


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def is_sorted(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True


def pugalo(array, arm_len) -> bool:

    ostatki_array = []

    for i in range(arm_len):
        ostatki_array.append([])

    for i in range(len(array)):
        ostatki_array[i % arm_len].append(array[i])

    for i in range(arm_len):
        randomize_quicksort(ostatki_array[i], 0, len(ostatki_array[i])-1)

    for i in range(len(array) - 1):
        j = i + 1
        if (ostatki_array[i % arm_len][i // arm_len]
                > ostatki_array[j % arm_len][j // arm_len]):
            return False
    return True


if __name__ == '__main__':
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')
    array = read_file_line(path_input, 1)
    array = list(map(int, array.split()))

    array_nums = read_file_line(path_input, 0)
    array_nums = list(map(int, array_nums.split()))

    answer = pugalo(array, array_nums[1])

    write_file(path_output, str(answer))
    print(f"task3 записан {answer}")
