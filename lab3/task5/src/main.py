import os

from lab3.utils import randomize_quicksort, reverse


def h_index(array: list[int]):

    randomize_quicksort(array, 0, len(array)-1)
    reverse(array)

    index = 0
    for i in range(len(array)):
        if array[i] >= i + 1:
            index = i + 1
        else:
            break

    return index


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]


if __name__ == '__main__':
    from lab3.utils import read_file_line, write_file, normVid
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    array = read_file_line(path_input, 0)
    array = list(map(int, array.split()))

    H = h_index(array)

    write_file(path_output, str(H))
    print(f"task1 записан {H}")
