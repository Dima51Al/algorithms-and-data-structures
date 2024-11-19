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
    array = [random.randint(1, 10) for i in range(10**5)]
    randomize_quicksort(array, 0, len(array)-1)
    print(len(array), array == sorted(array))
