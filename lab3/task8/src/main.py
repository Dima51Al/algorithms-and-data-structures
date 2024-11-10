# main.py
import random


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


def randomize_quicksort_in_turple(array, left, right, index_sort):
    # Рекурсивный вызов для подмассивов

    if left < right:
        key = random.randint(left, right - 1)
        swap(array, left, key)

        grow_then, less_then = partition(array, left, right, index_sort)
        randomize_quicksort_in_turple(array, left, less_then - 1, index_sort)
        randomize_quicksort_in_turple(array, grow_then + 1, right, index_sort)


def rast(a, b):
    return (a**2+b**2)**0.5


def main(array: list[list], k: int):
    for i in range(len(array)):
        array[i].append(rast(array[i][0], array[i][1]))
    randomize_quicksort_in_turple(array, 0, len(array)-1, 2)
    array_answer = []
    for i in range(k):
        array_answer.append(array[i][0:2])

    return array_answer


if __name__ == '__main__':
    print(main([[3, 3], [5, -1], [-2, 4]], 2))
