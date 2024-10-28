from lab1.utils import *


def lineSearch(array, index):
    indexes = []
    for i in range(len(array)):
        if array[i] == index:
            indexes.append(i)

    if len(indexes) == 1:
        return indexes[0]

    if len(indexes) == 0:
        return -1
    return indexes

def main():
    file = read_file_line(path_input, 1)

    array = list(map(int, file.split()))

    write_file(str(lineSearch(array, 0)))

if __name__ == '__main__':
    main()
