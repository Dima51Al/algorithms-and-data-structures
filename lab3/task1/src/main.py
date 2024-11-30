import os.path
import random
from random import randint


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right):
    x = array[left]
    j = left
    for i in range(left + 1, right):
        if array[i] <= x:
            j = j + 1
            swap(array, j, i)
    swap(array, left, j)
    return j


def quicksort(array, left, right):
    if left < right:
        m = partition(array, left, right)
        quicksort(array, left, m)
        quicksort(array, m + 1, right)


def randomize_quicksort(array, left, right):
    if left < right:
        key = randint(left, right - 1)
        swap(array, left, key)
        m = partition(array, left, right)
        randomize_quicksort(array, left, m)
        randomize_quicksort(array, m + 1, right)
    return array



if __name__ == '__main__':
    from lab3.utils import read_file_line, write_file, normVid
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    array = read_file_line(path_input, 1)
    array = list(map(int, array.split()))

    randomize_quicksort(array, 0, len(array))

    write_file(path_output, normVid(array))
    print(f"task1 записан {array}")

