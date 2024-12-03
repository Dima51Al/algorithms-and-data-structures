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


        def __init__(self, left, duration, right):
            self.left = left
            self.duration = duration
            self.right = right



    queue_array: set[Elem] = set()

    first: Elem = None
    last: Elem = None

    queue_limit = 10 ** 6
    length_queue = 0


    def isEmpty(self) -> bool:
        return self.length_queue == 0

    def push(self, duration):

        if self.length_queue >= self.queue_limit:
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

            answer = self.first.start
            self.queue_array.remove(self.first)
            self.length_queue -= 1
            self.last = None
            self.first = None

            print(answer)

            return answer

        #     else

        answer = self.first.start

        self.first = self.first.right
        self.queue_array.remove(self.first.left)
        self.first.left = None
        self.length_queue -= 1

        print(answer)
        return answer

    def init_after_start(self, msec):
        if self.first is None:
            return
        self.first.finish = self.first.duration + msec
        self.first.start = msec


def main(array: list[list], S):
    sort_double_array(array)

    if len(array) == 0:
        return

    queue = QueueModified()
    queue.limit_queue = S

    INDEX = 0
    milisec = 0

    while milisec < 10**5:

        if INDEX < len(array):
            elem = array[INDEX]

        if elem[0] == milisec:

            queue.push(elem[1])
            if queue.length_queue == 1:
                queue.init_after_start(milisec)
            INDEX += 1


        if queue.first is None:
            return

        if milisec == queue.first.finish:
            queue.pop()
            queue.init_after_start(milisec)

        milisec += 1


if __name__ == '__main__':
    array = [[i, 2] for i in range(6)]
    main(array, 3)

    array = [[0, 0], [0, 0]]
    main(array, 1)

