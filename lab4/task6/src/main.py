import os
from lab4.utils import min_max


def take_from_queue_with_min(queue: list):
    """
    queue[0] - is number the first element
    queue[1] - is a max element
    queue[2] - is count of max element
    """
    if len(queue) == 1:
        return None

    answer = queue[queue[0] + 2]

    if answer == queue[1]:
        queue[2] -= 1

    if queue[2] == 0:
        queue[1] = min_max(queue[3:], 1)[0]


    queue[0] = queue[0] + 1

    return answer


def put_to_queue_with_min(queue: list[int], elem):

    queue.append(elem)

    if elem < queue[1]:
        queue[1] = elem
        queue[2] = 1

    elif elem == queue[1]:
        queue[2] += 1


def min_from_queue(queue):
    return queue[1]



def init_queue_with_min():

    return [1, 2*10**9, 1]


if __name__ == '__main__':
    queue_array = init_queue_with_min()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')


    def read_func(string: str):
        if "+" in string:
            value = int(string.split()[1])
            put_to_queue_with_min(queue_array, value)
        elif string == "-":
            answer_array.append(take_from_queue_with_min(queue_array))
        else:
            answer_array.append(min_from_queue(queue_array))


    from lab4.utils import read_file_line, write_file, normVid

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        read_func(read_file_line(path_input, i+1))

    write_file(path_output, normVid(answer_array))
