from random import random, randint


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
    with open("output.txt", "a") as file:
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


N = 10 ** 5
# array = [randint(1, 10**9) for i in range(N)]
array = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
with open("output.txt", "w") as file:
    file.write("")
    file.close()


def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


a = merge_sort(array, 0, len(array))
with open("output.txt", "a") as file:
    file.write(normVid(a))
    file.close()
