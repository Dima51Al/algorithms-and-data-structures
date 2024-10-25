def swap_neighboring(array, i):
    array[i], array[i - 1] = array[i - 1], array[i]
    return array
def insertionSort(array) -> None:
    length = len(array)
    for index in range(1, length):
        tmp = index
        while array[tmp] > array[tmp - 1]:
            swap_neighboring(array, tmp)
            tmp -= 1
            if tmp == 0:
                break
    return array
