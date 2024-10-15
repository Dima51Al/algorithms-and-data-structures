def lineSearch() ->  None:
    file = open("input.txt").readlines()[0]
    elem = int(open("input.txt").readlines()[1])
    array = list(map(int, file.split()))
    indexes: list[int] = []

    for i in range(len(array)):
        if array[i] == elem:
            indexes.append(i)
    if len(indexes) == 0:
        open("output.txt", "w").write(str(-1))
        return
    if len(indexes) == 1:
        open("output.txt", "w").write(str(indexes)[0])
        return
    open("output.txt", "w").write(str(indexes)[1:-1])
