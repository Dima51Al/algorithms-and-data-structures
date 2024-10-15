import random


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
        with open("output.txt", "a") as file:
            file.write(str(left) + " ")
        return left
    with open("output.txt", "a") as file:
        file.write(str(-1) + " ")
    return -1


file = open("input.txt").readlines()[1]

array = list(map(int, file.split()))

file = open("input.txt").readlines()[3]

values = list(map(int, file.split()))

with open("output.txt", "w") as file:
    file.write(" ")
[binSearch(array, i) for i in values]
