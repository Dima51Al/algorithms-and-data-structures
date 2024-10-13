def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0 for _ in range(1, n1 + 1)]
    R = [0 for _ in range(1, n2 + 1)]

    for i in range(n1):
        L[i] = array[p + i - 1]

    for j in range(n2):
        R[j] = array[q + j]
    L.append(1000000000)
    R.append(1000000000)
    i, j = 0, 0

    for k in range(p, r):
        # if len(L) == i:
        #     array[k] = R[j]
        #     j += 1
        #     break
        # if len(R) == j:
        #     array[k] = L[i]
        #     i += 1
        #     break

        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
    print(array, p, q, r)

def merge_sort(array: list[int], p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)
        return array




a = [i for i in range(16, 0, -1)]

print(a)
merge_sort(a, 0, 16)
print(a)

