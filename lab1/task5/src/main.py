import copy
from lab1.utils import *


def selectionSort(array) -> list[int]:

    array = copy.deepcopy(array)
    sorted_array: list[int] = []

    for i in range(len(array)):
        sorted_array.append(array.pop(min_max(array, 1)[1]))

    return sorted_array


def main():
    file = read_file_line(path_input, 1)

    array = list(map(int, file.split()))

    write_file(str(selectionSort(array)))


if __name__ == '__main__':
    main()
