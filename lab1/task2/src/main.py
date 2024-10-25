def normVid(array: list) -> str:
    s = ""
    for i in range(len(array) - 1):
        s += str(array[i]) + " "
    s += str(array[-1])
    return s


def insertionSort() -> None:
    file = open("../txtf/input.txt").readlines()[1]
    array = list(map(int, file.split()))
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
        string_output = normVid(b) + "\n" + normVid(array)
    open("../txtf/output.txt", "w").write(string_output)
