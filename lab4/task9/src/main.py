import os


class Queue:
    class Elem:
        left = None
        value = None
        right = None

        def __init__(self, left, value, right):
            self.left = left
            self.value = value
            self.right = right

        def info(self, string=""):
            print(string, end="")
            if self.left is not None:
                print(self.left.value, end=" ")
            else:
                print("-", end=" ")
            print(self.value, end=" ")
            if self.right is not None:
                print(self.right.value)
            else:
                print("-")

    queue_array: set[Elem] = set()
    first: Elem = None
    center: Elem = None
    last: Elem = None
    len_queue = 0

    def __init__(self, array=None):
        if array is None:
            array = []
        for queue_elem in array:
            self.enqueue(queue_elem)

    def isEmpty(self) -> bool:
        return self.len_queue == 0

    def enqueue(self, *args):
        for queue_elem in args:
            if self.isEmpty():
                elem = self.Elem(None, queue_elem, None)
                self.first = elem
                self.center = elem
                self.last = elem
                self.queue_array.add(elem)
                self.len_queue += 1
            else:
                elem = self.Elem(self.last, queue_elem, None)
                self.last.right = elem
                self.last = elem
                self.queue_array.add(elem)
                self.len_queue += 1
                if self.len_queue % 2 == 1:
                    self.center = self.center.right

    def center_push(self, value):
        elem = self.Elem(self.center, value, self.center.right)
        if self.center.right is not None:
            self.center.right.left = elem
        else:
            self.last = elem
        self.center.right = elem
        self.queue_array.add(elem)
        self.len_queue += 1
        if self.len_queue % 2 == 1:
            self.center = self.center.right

    def dequeue(self) -> Elem.value:
        if not self.isEmpty():
            elem = self.first
            self.queue_array.remove(elem)
            self.first = elem.right
            self.len_queue -= 1
            if self.len_queue % 2 == 1:
                self.center = self.center.right
            if not self.isEmpty():
                if self.first is not None:
                    self.first.left = None
            else:
                self.first = None
                self.center = None
                self.last = None
            return elem.value

    def get_array(self) -> list:
        array = []
        if self.isEmpty():
            return array
        elem = self.first
        while elem.right is not None:
            array.append(elem.value)
            elem = elem.right
        array.append(elem.value)
        return array

    def queue_info(self):
        if self.isEmpty():
            print("Queue empty")
            return
        self.first.info("first:\n")
        self.center.info("center:\n")
        self.last.info("last:\n")
        print("\nvalues:")
        print(self.get_array())
        print("\n\nelements (left, value, right):")
        queue_elem = self.first
        while queue_elem is not None:
            queue_elem.info()
            queue_elem = queue_elem.right


if __name__ == '__main__':

    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

    queue_array = Queue()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    def read_func(string: str):
        if "+" in string:
            value = int(string.split()[1])
            queue_array.enqueue(value)
        elif "-" in string:
            answer_array.append(queue_array.dequeue())
        else:
            value = int(string.split()[1])
            queue_array.center_push(value)

    from lab4.utils import read_file_line, write_file, vertical_norm_view




    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        read_func(read_file_line(path_input, i + 1))

    answer = vertical_norm_view(answer_array)
    write_file(path_output, answer)
    print(answer)
