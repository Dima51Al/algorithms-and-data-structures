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


if __name__ == '__main__':
    print(main(["acd", "zab", "baa", "bab", "bbb"]))
