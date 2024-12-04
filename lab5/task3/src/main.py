import os


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, left, right, index_sort):
    x = array[left][index_sort]
    less_then = left
    grow_then = right
    i = left + 1

    while i <= grow_then:
        if array[i][index_sort] < x:
            swap(array, less_then, i)
            less_then += 1
            i += 1
        elif array[i][index_sort] > x:
            swap(array, grow_then, i)
            grow_then -= 1
        else:
            i += 1
    return grow_then, less_then


def quicksort_in_smth(array, left, right, index_sort):
    if left < right:
        grow_then, less_then = partition(array, left, right, index_sort)
        quicksort_in_smth(array, left, less_then - 1, index_sort)
        quicksort_in_smth(array, grow_then + 1, right, index_sort)


def sort_double_array(array):
    """ [[1, 1], [1, 1], ... ] """
    quicksort_in_smth(array, 0, len(array) - 1, 1)
    quicksort_in_smth(array, 0, len(array) - 1, 0)
    return array


class QueueModified:
    class Elem:
        left = None

        start = None
        duration = None
        finish = None

        right = None

        count_of_heartbroken = 0

        def __init__(self, left, duration, right):
            self.left = left
            self.duration = duration
            self.right = right

    queue_array: set[Elem] = set()

    first: Elem = None
    last: Elem = None

    queue_limit = 10 ** 6
    length_queue = 0

    def minus_heart(self):
        self.first.count_of_heartbroken -= 1

    def set_limit(self, limit=10 ** 6):
        self.queue_limit = limit

    def isEmpty(self) -> bool:
        return self.length_queue == 0

    def push(self, duration):

        if self.length_queue == self.queue_limit:
            self.last.count_of_heartbroken += 1

            return

        elem = self.Elem(None, duration, None)

        if self.isEmpty():
            self.queue_array.add(elem)
            self.first = elem
            self.last = elem

        else:
            elem.left = self.last
            self.last.right = elem
            self.last = elem
            self.queue_array.add(elem)

        self.length_queue += 1

    def __init__(self, arr=None):
        if arr is None:
            arr = []

        for elem in arr:
            self.push(elem)

    def pop(self):

        if self.isEmpty():
            return

        if self.length_queue == 1:
            answer = [self.first.start, self.first.count_of_heartbroken]

            self.queue_array.remove(self.first)
            self.length_queue -= 1
            self.last = None
            self.first = None

            return answer

        #     else

        answer = [self.first.start, self.first.count_of_heartbroken]

        self.first = self.first.right
        self.queue_array.remove(self.first.left)
        self.first.left = None
        self.length_queue -= 1

        return answer

    def init_after_start(self, msec):
        if self.first is None:
            return
        self.first.finish = self.first.duration + msec
        self.first.start = msec

    def get_array(self) -> list:
        arr = []
        if self.isEmpty():
            return arr

        elem = self.first

        while elem.right is not None:
            arr.append([elem.duration, elem.count_of_heartbroken])
            elem = elem.right

        arr.append([elem.duration, elem.count_of_heartbroken])

        return arr

    def check_time(self, time):
        if self.isEmpty():
            return
        answer = list()

        while not self.isEmpty():
            if time == self.first.finish:

                value = self.pop()
                decoder(value, answer)

                self.init_after_start(time)
            else:
                break
        return answer


def decoder(arr1: list, array: list):
    array.append(arr1[0])
    if arr1[1] != 0:
        for i in range(arr1[1]):
            array.append(-1)


def main(array: list[list], S):
    answer_array_main = []

    sort_double_array(array)

    if len(array) == 0:
        return

    queue = QueueModified()
    queue.set_limit(S)

    INDEX = 0
    milisec = 0

    while milisec < 17:
        tmp_arr = queue.check_time(milisec)
        if tmp_arr is not None:
            answer_array_main += tmp_arr

        if INDEX < len(array):
            while array[INDEX][0] == milisec:

                queue.push(array[INDEX][1])

                if queue.length_queue == 1:
                    queue.init_after_start(milisec)

                INDEX += 1
                if INDEX == len(array):
                    break

        tmp_arr = queue.check_time(milisec)
        if tmp_arr is not None:
            answer_array_main += tmp_arr

        milisec += 1

    return answer_array_main


if __name__ == '__main__':
    from lab5.utils import read_file_line, write_file, vertical_norm_view

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    S, n = list(map(int, read_file_line(path_input, 0).split()))

    array = [list(map(int, read_file_line(path_input, i + 1).split())) for i in range(n)]
    answer_array = main(array, S)

    write_file(path_output, vertical_norm_view(answer_array))
