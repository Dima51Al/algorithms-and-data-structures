import os


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right, index_sort):
    x = array[left][index_sort]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i][index_sort] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i][index_sort] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def quicksort_in_str(array, left, right, index_sort):
    if left < right:
        grow_then, less_then = partition(array, left, right, index_sort)
        quicksort_in_str(array, left, less_then - 1, index_sort)
        quicksort_in_str(array, grow_then + 1, right, index_sort)





def main(array: list[str]):
    if len(array) == 0:
        return array
    for i in range(len(array[0])-1, -1, -1):
        quicksort_in_str(array, 0, len(array) - 1, i)
    return array


def partition_with_tuple_with_index(array, left, right, index_sort, index_value):
    x = array[left][index_value][index_sort]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i][index_value][index_sort] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i][index_value][index_sort] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def quicksort_in_str_with_tuple_with_index(array, left, right, index_sort, index_value):
    if left < right:
        grow_then, less_then = partition_with_tuple_with_index(array, left, right, index_sort, index_value)
        quicksort_in_str_with_tuple_with_index(array, left, less_then - 1, index_sort, index_value)
        quicksort_in_str_with_tuple_with_index(array, grow_then + 1, right, index_sort, index_value)


def main_with_index(array: list[str], index: int):
    """[(abc, 1), (bax, 2), (asd, 3), (asd, 4)] index = 0"""

    if len(array) == 0:
        return array

    for i in range(len(array[0][index])-1, -1, -1):
        quicksort_in_str_with_tuple_with_index(array, 0, len(array) - 1, i, index)
    answer_arr = [i[1] for i in array]
    return answer_arr


def vertical_to_horizontal(vertical_data):
    rows = len(vertical_data)
    cols = len(vertical_data[0])
    horizontal_data = [''.join(vertical_data[row][col] for row in range(rows)) for col in range(cols)]
    return horizontal_data


if __name__ == '__main__':
    from lab3.utils import read_file_line, write_file, normVid

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    n = read_file_line(path_input, 0)
    n = n.split()
    n = n[0]
    n = int(n)

    input_data = []


    for i in range(1, n + 1):
        input_data.append(read_file_line(path_input, i).replace("\n", "").replace(" ", ""))
    input_data_tmp = vertical_to_horizontal(input_data)
    input_data = []
    for i in range(len(input_data_tmp)):
        input_data.append((input_data_tmp[i], i+1))

    answer = main_with_index(input_data, 0)

    write_file(path_output, normVid(answer))
    print(f"task1 записан {answer}")
