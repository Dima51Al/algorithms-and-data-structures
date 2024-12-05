import hashlib
import os


class HashSet:
    main_set = set()

    def coder(self, value):
        return hashlib.sha256(str(value).encode()).hexdigest()

    def replace(self, elem, index):
        """index: 0 == A, 1 == B"""
        import hashlib
        elem = str(elem)
        hashed = hashlib.sha256(elem.encode()).hexdigest()
        if not index:
            self.A = hashed
        else:
            self.B = hashed

    def add(self, elem):
        self.main_set.add(self.coder(elem))

    def is_in(self, elem):
        hashed = self.coder(elem)
        return hashed in self.main_set


def main(N, X, A, B, AC, BC, AD, BD):
    queue_array = HashSet()
    for i in range(N):
        if not queue_array.is_in(X):
            queue_array.add(X)
            A = (A + AD) % 10 ** 3
            B = (B + BD) % 10 % 15
        else:
            A = (A + AC) % 10 ** 3
            B = (B + BC) % 10 % 15
        X = (X * A + B) % 10 ** 15

    return [X, A, B]


if __name__ == '__main__':
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    from lab6.utils import read_file_line, write_file, normVid

    N, X, A, B = list(map(int, read_file_line(path_input, 0).split()))
    AC, BC, AD, BD = list(map(int, read_file_line(path_input, 1).split()))

    answer_array = main(N, X, A, B, AC, BC, AD, BD)
    write_file(path_output, normVid(answer_array))
