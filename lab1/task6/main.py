def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


def Bubble_sort():
    file = open("input.txt").readlines()[1]
    array = list(map(int, file.split()))
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            if array[j] < array[j-1]:
                array[j], array[j - 1] = array[j-1], array[j]
    open("output.txt", "w").write(normVid(array))
