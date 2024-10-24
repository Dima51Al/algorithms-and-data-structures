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
