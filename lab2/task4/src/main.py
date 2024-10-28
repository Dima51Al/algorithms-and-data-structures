from lab2.utils import *


def binSearch(array: list[int], number: int):
    left = 0
    right = len(array)

    while right - left > 1:
        center = (left + right) // 2
        if array[center] <= number:
            left = center
        else:
            right = center
    if array[left] == number:
        return left
    return -1


def array_bin_search(array, values) -> list[int]:
    return [binSearch(array, i) for i in values]

def main():
    file_0 = read_file_line(path_input, 1)
    file_1 = read_file_line(path_input, 3)
    array = list(map(int, file_0.split()))
    values = list(map(int, file_1.split()))
    write_file(normVid(array_bin_search(array, values)))

if __name__ == '__main__':
    main()
