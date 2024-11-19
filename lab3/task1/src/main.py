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


if __name__ == '__main__':
    array = [6, 4, 8, 2, 9, 3, 9, 4, 7, 6, 1]
    randomize_quicksort(array, 0, len(array))
    print(array == sorted(array))
