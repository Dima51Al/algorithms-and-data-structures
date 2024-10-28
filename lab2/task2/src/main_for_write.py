from lab2.utils import *


def merge(array: list[int], left: int, center: int, right: int) -> list[int]:
    left_array = array[left:center]
    right_array = array[center:right]
    id_left = 0
    id_right = 0

    left_array.append(2 ** 62 - 1)
    right_array.append(2 ** 62 - 1)

    for key in range(left, right):
        if left_array[id_left] <= right_array[id_right]:
            array[key] = left_array[id_left]
            id_left += 1
        else:
            array[key] = right_array[id_right]
            id_right += 1
    with open("../txtf/output.txt", "a") as file:
        file.write(f'{left + 1} {right} {array[left]} {array[right - 1]}\n')
        file.close()
    return array


def merge_sort(array: list[int], left, right) -> list[int]:
    if right - left != 1:
        center = (left + right) // 2

        merge_sort(array, left, center)
        merge_sort(array, center, right)

        merge(array, left, center, right)

    return array


def main():
    file = read_file_line(path_input, 1)

    array = list(map(int, file.split()))

    write_file(str(merge_sort(array, 0, len(array))))

if __name__ == '__main__':
    main()

