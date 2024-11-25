import os
import random


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right):
    x = array[left]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def randomize_quicksort(array, left, right):
    # Рекурсивный вызов для подмассивов

    if left < right:
        key = random.randint(left, right - 1)
        swap(array, left, key)

        grow_then, less_then = partition(array, left, right)
        randomize_quicksort(array, left, less_then - 1)
        randomize_quicksort(array, grow_then + 1, right)


if __name__ == '__main__':
    from lab3.utils import read_file_line, write_file, normVid
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    array = read_file_line(path_input, 1)
    array = list(map(int, array.split()))

    randomize_quicksort(array, 0, len(array)-1)

    write_file(path_output, normVid(array))
    print(f"task1 записан {array}")