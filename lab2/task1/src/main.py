# merge
import random


def merge(array: list[int], left: int, center: int, right: int) -> list[int]:

    left_array = array[left:center]
    right_array = array[center:right]
    id_left = 0
    id_right = 0

    left_array.append(2**62 - 1)
    right_array.append(2**62 - 1)



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
        center = (left+right)//2

        merge_sort(array, left, center)
        merge_sort(array, center, right)

        merge(array, left, center, right)


    return array



# a = [i for i in range(16, 0, -1)]
# merge_sort(a, 0, 16)


# a = [random.randint(1, 10) for i in range(10, 0, -1)]
# a = [9, 7, 5, 8]
# a = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
# merge_sort(a, 0, len(a))
