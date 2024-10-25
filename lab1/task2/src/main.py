def insertionSort(array) -> list[list]:
    length = len(array)
    b = []
    for index in range(length):
        tmp = index
        while array[tmp] < array[tmp - 1]:
            array[tmp], array[tmp - 1] = array[tmp - 1], array[tmp]
            tmp -= 1
            if tmp == 0:
                break
        b.append(tmp + 1)
    return [b, array]
