import hashlib
import os
import sys


class HashSet:
    main_set = set()
    first = 1
    second = 1

    def add(self, elem):
        import hashlib
        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()
        self.main_set.add(hashed)

    def __init__(self):
        self.main_set.add(1)

    def next(self):
        tmp = self.second
        self.second += self.first
        self.first = tmp

        self.add(str(self.first))


    def is_in(self, elem):
        import hashlib
        elem = int(elem)

        while self.second <= elem:
            self.next()

        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()

        return hashed in self.main_set


if __name__ == '__main__':
    from lab6.utils import read_file_line, write_file, vertical_norm_view
    queue_array = HashSet()

    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        answer_array.append(queue_array.is_in(read_file_line(path_input, i + 1)))

    write_file(path_output, vertical_norm_view(answer_array))
