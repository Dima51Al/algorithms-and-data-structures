import os


def is_heap(array: list) -> bool:
    for i in range(1, len(array)//2+1):
        if array[i-1] > array[2*i-1]:
            return False
        if array[i-1] > array[2*i]:
            return False
    return True


def main(array) -> str:

    if is_heap(array):
        return "YES"
    return "NO"


if __name__ == '__main__':
    from lab5.utils import read_file_line, write_file

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    array = read_file_line(path_input, 0).split()
    array = list(map(int, array))

    answer = main(array)

    write_file(path_output, answer)
