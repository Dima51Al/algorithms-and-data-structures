import os


def intersection(array_second, array_first):
    def main(array_sovpadeniy, right_first, right_second):
        for i in range(right_first, len(array_first)):
            for j in range(right_second, len(array_second)):
                if array_first[i] == array_second[j]:
                    value = array_first[i]
                    array_sovpadeniy.append(value)
                    main(array_sovpadeniy, i+1, j+1)
                    return len(array_sovpadeniy)

    return main([], 0, 0)



if __name__ == '__main__':



    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')


    from lab7.utils import read_file_line, write_file, vertical_norm_view

    array_first = list(map(int, read_file_line(path_input, 1).split()))
    array_second = list(map(int, read_file_line(path_input, 3).split()))

    answer = str(intersection(array_first, array_second))

    write_file(path_output, answer)



