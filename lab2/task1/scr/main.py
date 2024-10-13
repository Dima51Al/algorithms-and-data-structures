# merge
import random


def merge(A: list[int], B: list[int]) -> list[int]:
    array = []
    la = len(A)
    lb = len(B)

    if la * lb == 0:
        if la == 0:
            array += B
        else:
            array += A
        return array

    while True:
        if A[0] < B[0]:
            array.append(A.pop(0))
            la -= 1
        else:
            array.append(B.pop(0))
            lb -= 1
        if la * lb == 0:
            if la == 0:
                array += B
            else:
                array += A
            return array


def merge_sort(array: list[int], p, r) -> list[int]:
    if p < r:

        q = (p + r) // 2
        # print(p, r)
        if r - p > 1:
            merge_sort(array[p:q], p, q)
            merge_sort(array[q:r], q, r)

        print(array[p:q], array[q:r])

        return array


# A = [1, 3, 5]
# B = [2, 4]
# print(merge(A, B))

a = [i for i in range(16, 0, -1)]
print(merge_sort(a, 1, 16))

