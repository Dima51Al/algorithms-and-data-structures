import copy

from lab1.utils import *


def Bubble_sort(array):
    array = copy.deepcopy(array)
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j-1] > array[j]:
                tmp_1 = array[j-1]
                tmp_2 = array[j]
                array[j-1], array[j] = tmp_2, tmp_1

    return array

def main():
    file = read_file_line(path_input, 1)

    array = list(map(int, file.split()))

    write_file(str(Bubble_sort(array)))

if __name__ == '__main__':
    main()
