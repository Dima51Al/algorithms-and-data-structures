import random
import time

import memory_profiler

path_input = "../txtf/input.txt"
path_output = "../txtf/output.txt"


def write_file(string: str) -> None:
    with open(path_output, "w", encoding="utf-8") as file:
        file.write(string)


def read_file() -> str:
    with open(path_input, "r") as file:
        return file.read()


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


def read_file_line(path: str, num: int) -> str:
    line = open(path, "r").readlines()[num]
    return line


def base_test(function, *args):
    """функция, аргумент1, аргумент2..."""
    memory_before = memory_profiler.memory_usage()[0]

    tmp = time.time()

    answer = function(*args)

    tmp = time.time() - tmp

    memory_after = memory_profiler.memory_usage()[0]

    print()
    print("Время выполнения: ", tmp, " сек")
    print("Использование памяти: ", memory_after - memory_before, "МБ")
    print()
    return answer


def min_max(array: list[int], mm: int) -> list[int]:
    """ массив; 1 если мин, -1 если макс | выход: [элемент, индекс]"""
    if len(array) == 0:
        return -1

    array1 = [array[0], 0]

    for i in range(len(array)):
        if mm * array[i] < mm * array1[0]:
            array1[0], array1[1] = array[i], i
    return array1


def random_array(length: int, min_value: int, max_value: int) -> list[int]:
    return [random.randint(min_value, max_value) for _ in range(length)]


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


def reverse(array: list[int]):
    second_array = []
    for i in range(len(array) - 1, -1, -1):
        second_array.append(array[i])
    for i in range(len(array)):
        array[i] = second_array[i]
