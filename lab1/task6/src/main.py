def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


def Bubble_sort():
    file = open("../txtf/input.txt").readlines()[1]
    array = list(map(int, file.split()))
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j-1] > array[j]:

                tmp_1 = array[j-1]
                tmp_2 = array[j]

                array[j-1], array[j] = tmp_2, tmp_1
            # print(array)
    open("../txtf/output.txt", "w").write(normVid(array))
