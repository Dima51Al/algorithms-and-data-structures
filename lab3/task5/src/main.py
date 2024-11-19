from lab3.utils import randomize_quicksort, reverse


def h_index(array: list[int]):

    randomize_quicksort(array, 0, len(array)-1)
    reverse(array)

    index = 0
    for i in range(len(array)):
        if array[i] >= i + 1:
            index = i + 1
        else:
            break

    return index


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(h_index(citations) == 3)
