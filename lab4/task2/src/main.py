import os


def take_from_queue(queue: list[int]):
    """queue[0] - is number the first element"""
    if len(queue) == 1:
        return None

    answer = queue[queue[0]]
    queue[0] = queue[0] + 1
    return answer


def put_to_queue(queue: list[int], elem):
    queue.append(elem)



def init_queue():
    return [1]


if __name__ == '__main__':
    queue_array = init_queue()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')


    def read_func(string: str):
        if string.count("-") == 0:
            value = int(string.split()[1])
            put_to_queue(queue_array, value)
        else:
            answer_array.append(take_from_queue(queue_array))

    from lab4.utils import read_file_line, write_file, normVid

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        read_func(read_file_line(path_input, i+1))

    write_file(path_output, normVid(answer_array))
