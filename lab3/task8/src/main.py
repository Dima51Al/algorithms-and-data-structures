# main.py
import os
import random

from lab3.utils import read_file_line, write_file, normVid


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right, index_sort):
    x = array[left][index_sort]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i][index_sort] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i][index_sort] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def randomize_quicksort_in_tuple(array, left, right, index_sort):
    # Рекурсивный вызов для подмассивов

    if left < right:
        key = random.randint(left, right - 1)
        swap(array, left, key)

        grow_then, less_then = partition(array, left, right, index_sort)
        randomize_quicksort_in_tuple(array, left, less_then - 1, index_sort)
        randomize_quicksort_in_tuple(array, grow_then + 1, right, index_sort)


def rast(a, b):
    return (a**2+b**2)**0.5


def main(array: list[list], k: int):
    for i in range(len(array)):
        array[i].append(rast(array[i][0], array[i][1]))
    randomize_quicksort_in_tuple(array, 0, len(array) - 1, 2)
    array_answer = []
    for i in range(k):
        array_answer.append(array[i][0:2])

    return array_answer


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')
    s = int(read_file_line(path_input, 0).split()[0])
    k = int(read_file_line(path_input, 0).split()[1])
    segment_array = []
    for i in range(s):
        x = int(read_file_line(path_input, i + 1).split()[0])
        y = int(read_file_line(path_input, i + 1).split()[1])
        segment_array.append([x, y])


    arr = main(segment_array, k)

    write_file(path_output, normVid(arr))
    print(f"task1 записан {arr}")
