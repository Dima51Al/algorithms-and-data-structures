import time

import memory_profiler


def write_file(path: str, string: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(string)


def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


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
    print("Время выполнения: ", tmp)
    print("Использование памяти: ", memory_after - memory_before, "МБ")
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

