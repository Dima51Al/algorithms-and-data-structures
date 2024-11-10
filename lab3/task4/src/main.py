# точки и отрезки

from lab3.utils import *

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right):
    x = array[left][0]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i][0] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i][0] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def randomize_quicksort_in_turple(array, left, right):
    # Рекурсивный вызов для подмассивов

    if left < right:
        key = random.randint(left, right - 1)
        swap(array, left, key)

        grow_then, less_then = partition(array, left, right)
        randomize_quicksort_in_turple(array, left, less_then - 1)
        randomize_quicksort_in_turple(array, grow_then + 1, right)


def binSearch(array: list[tuple], number: int):

    left = 0
    right = len(array)

    while right - left > 1:
        center = (left + right) // 2
        if array[center][0] > number:
            right = center
        else:
            left = center

    if array[left][0] <= number:
        return left + 1
    return 0


def main(segment_array: list[tuple], dot_array) -> list[int]:
    """на вход список из отрезков вида (a, b); список из точек """
    randomize_quicksort_in_turple(segment_array, 0, len(segment_array) - 1)
    dot_array_answer = []

    for i in range(len(dot_array)):
        dot_array_answer.append(0)

    for dot_index in range(len(dot_array)):
        for i in range(0, binSearch(segment_array, dot_array[dot_index])):
            if segment_array[i][1] >= dot_array[dot_index]:
                dot_array_answer[dot_index] += 1


    return dot_array_answer



if __name__ == '__main__':
    print(main([(1, 2)], [0, 1.5, 2, 3]) == [0, 1, 1, 0])