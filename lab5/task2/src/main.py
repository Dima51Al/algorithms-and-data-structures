import os
import sys


def do_array_to_parents_view(array: list[int]):
    """
    поступает массив. например
    [-1, 0, 4, 0, 3] - массив
    [ 0, 1, 2, 3, 4] - индексы
    -1 означает, то 0 - вершина
    0 у 1 и 3 означает, то 1 и 3 исходят из 0
    """



    n = len(array)

    arr: list[list] = [[] for _ in range(n)]

    for i in range(n):
        tmp = array[i]
        if tmp == -1:
            continue
        arr[tmp].append(i)
    return arr


def recursion_sum_len(arr=None):

    if arr is None:
        arr = []

    if type(arr) is int:
        return 0

    if len(arr) == 0:
        return 0

    return 1 + sum([recursion_sum_len(i) for i in arr])


def main(main_array: list[int]):
    sys.setrecursionlimit(10 ** 5 + 1)
    main_array = do_array_to_parents_view(main_array)
    answer = recursion_sum_len(main_array)
    return answer


if __name__ == '__main__':
    from lab5.utils import read_file_line, write_file

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    array = read_file_line(path_input, 0).split()
    array = list(map(int, array))

    answer_array = main(array)

    write_file(path_output, str(answer_array))
