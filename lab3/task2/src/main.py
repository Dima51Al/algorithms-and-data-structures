# main.py
import time


def qsort(array, left, right, count):
    key = array[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        count+=1
        while array[i] < key:  # first while
            count+=1
            i += 1
        while array[j] > key:  # second while
            count+=1
            j -= 1
        if i <= j:
            count+=1
            array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    if left < j:
        count += 1
        qsort(array, left, j, count)
    if i < right:
        count+=1
        qsort(array, i, right, count)
    return count


def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

t = 0
for leN in range(1, 10**4):


    t -= time.time()
    array = [i for i in range(leN - 1, -1, -1)]
    t += time.time()

    qsort(array, 0, len(array)-1, 0)
print(t)
was = 32