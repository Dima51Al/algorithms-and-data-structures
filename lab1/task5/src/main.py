def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


def min_max(array: list[int], mm: int) -> int:
    """ массив; 1 если мин, -1 если макс"""
    if len(array) == 0:
        return -1

    array1 = [array[0], 0]

    for i in range(len(array)):
        if mm * array[i] < mm * array1[0]:
            array1[0], array1[1] = array[i], i
    return array1[1]





def selectionSort() -> None:
    file = open("input.txt").readlines()[0]
    array = list(map(int, file.split()))
    sorted_array: list[int] = []

    for i in range(len(array)):
        sorted_array.append(array.pop(min_max(array, 1)))
    open("output.txt", "w").write(str(normVid(sorted_array)))


