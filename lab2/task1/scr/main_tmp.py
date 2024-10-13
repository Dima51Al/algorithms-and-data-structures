def merge(array, p, q, r):
    n1 = q - p
    n2 = r - q

    L = [i for i in range(n1)]
    R = [i for i in range(n2)]

    for i in range(n1):
        L[i] = array[p + i]

    for i in range(n2):
        R[i] = array[q + i]


    print(L, R)
    i, j = 0, 0
    for k in range(p, r-1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


def merge_sort(array: list[int], p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)
        return array


a = [i for i in range(16, 0, -1)]
print(merge_sort(a, 0, 16))

