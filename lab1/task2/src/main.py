from lab1.utils import *


def insertionSort(array) -> list[list]:
    length = len(array)
    b = []
    for index in range(length):
        tmp = index
        while array[tmp] < array[tmp - 1]:
            array[tmp], array[tmp - 1] = array[tmp - 1], array[tmp]
            tmp -= 1
            if tmp == 0:
                break
        b.append(tmp + 1)
    return [b, array]

def main():
    file = read_file_line(path_input, 1)

    array = list(map(int, file.split()))

    write_file(str(insertionSort(array)))

if __name__ == '__main__':
    main()