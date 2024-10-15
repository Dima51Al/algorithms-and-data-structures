def merge(array: list[int], left: int, center: int, right: int) -> int:
    left_array = array[left:center]
    right_array = array[center:right]
    id_left = 0
    id_right = 0

    left_array.append(2 ** 62 - 1)
    right_array.append(2 ** 62 - 1)

    res = 0


    for key in range(left, right):
        if left_array[id_left] <= right_array[id_right]:
            array[key] = left_array[id_left]
            id_left += 1
            res += (key - center)
        else:
            res += (center - key)


            array[key] = right_array[id_right]
            id_right += 1

    return res


def merge_sort(array: list[int], left, right) -> int:
    if right - left != 1:
        center = (left + right) // 2

        res = merge_sort(array, left, center)
        res += merge_sort(array, center, right)
        res += merge(array, left, center, right)
        return res

    return 0


