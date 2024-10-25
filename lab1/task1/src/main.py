def insertionSort(array) -> None:
    length = len(array)
    for index in range(1, length):
        tmp = index
        while array[tmp] < array[tmp - 1]:
            array[tmp], array[tmp - 1] = array[tmp - 1], array[tmp]
            tmp -= 1
            if tmp == 0:
                break
    return array
