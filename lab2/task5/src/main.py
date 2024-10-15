import random
import time


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
    return array


def merge_sort(array: list[int], left, right) -> list[int]:
    if right - left != 1:
        center = (left + right) // 2

        merge_sort(array, left, center)
        merge_sort(array, center, right)

        merge(array, left, center, right)

    return array


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


def majority(array: list[int]):
    sorted_array = merge_sort(array, 0, len(array))
    lenght = len(sorted_array)

    variable = sorted_array[lenght // 2]

    left, right = 0, 0
    for i in range(lenght):
        if sorted_array[i] == variable:
            left = i
            break
    for i in range(lenght - 1, -1, -1):
        if sorted_array[i] == variable:
            right = i
            break
    if right - left < lenght // 2:
        return 0
    return 1


def main():
    with open("input.txt") as file:
        array = list(map(int, file.readlines()[1].split()))
        file.close()

    with open("output.txt", "w") as file:
        file.write(str(majority(array)))