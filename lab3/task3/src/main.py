# сортировка пугалом

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
    print(pugalo([1, 5, 3, 4, 1], 3))
