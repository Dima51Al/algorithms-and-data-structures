# merge
import random


def merge(array: list[int], left: int, center: int, right: int) -> list[int]:

    left_array = array[left:center]
    right_array = array[center:right]


    for key in range(left, right):


        if len(left_array) == 0:
            array[key] = right_array.pop(0)
            continue
        if len(right_array) == 0:
            array[key] = left_array.pop(0)
            continue

        if left_array[0] <= right_array[0]:
            array[key] = left_array.pop(0)
        else:
            array[key] = right_array.pop(0)
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
#
# for i in range(1000):
#     a = [random.randint(1, 10) for i in range(32, 0, -1)]
#     merge_sort(a, 0, 32)
#     if a == sorted(a):
#         continue
#     print("asdasd")

