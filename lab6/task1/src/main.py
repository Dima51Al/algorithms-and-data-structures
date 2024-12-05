import os


class HashSet:
    main_set = set()


    def add(self, elem):
        import hashlib
        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()
        self.main_set.add(hashed)


    def remove(self, elem):
        import hashlib
        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()
        self.main_set.remove(hashed)


    def is_in(self, elem):
        import hashlib
        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()
        return hashed in self.main_set


if __name__ == '__main__':
    queue_array = HashSet()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')


    def read_func(string: str):
        if "A" in string:
            value = int(string.split()[1])
            queue_array.add(value)
        elif "D" in string:
            value = int(string.split()[1])
            queue_array.remove(value)
        else:
            value = int(string.split()[1])
            if queue_array.is_in(value):
                answer_array.append("Y")
            else:
                answer_array.append("N")


    from lab6.utils import read_file_line, write_file, vertical_norm_view

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        read_func(read_file_line(path_input, i + 1))

    write_file(path_output, vertical_norm_view(answer_array))
