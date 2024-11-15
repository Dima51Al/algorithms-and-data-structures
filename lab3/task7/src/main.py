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


def randomize_quicksort_in_str(array, left, right, index_sort):
    # Рекурсивный вызов для подмассивов

    if left < right:
        key = random.randint(left, right - 1)
        swap(array, left, key)

        grow_then, less_then = partition(array, left, right, index_sort)
        randomize_quicksort_in_str(array, left, less_then - 1, index_sort)
        randomize_quicksort_in_str(array, grow_then + 1, right, index_sort)





def main(array: list[str]):
    for i in range(len(array[0])-1, -1, -1):
        randomize_quicksort_in_str(array, 0, len(array) - 1, i)


    return array


if __name__ == '__main__':
    print(main(["bab", "bba", "baa"]))
