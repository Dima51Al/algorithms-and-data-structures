import copy
from utils import *


def selectionSort(array) -> list[int]:

    array = copy.deepcopy(array)
    sorted_array: list[int] = []

    for i in range(len(array)):
        sorted_array.append(array.pop(min_max(array, 1)[1]))

    return sorted_array
