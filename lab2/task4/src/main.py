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


def array_bin_search(array, values) -> list[int]:
    return [binSearch(array, i) for i in values]
