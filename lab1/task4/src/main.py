def lineSearch(array, index):
    indexes = []
    for i in range(len(array)):
        if array[i] == index:
            indexes.append(i)

    if len(indexes) == 1:
        return indexes[0]

    if len(indexes) == 0:
        return -1
    return indexes


