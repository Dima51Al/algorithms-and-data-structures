import os


def put_to_stack(stack_array: list, elem):
    stack_array.append(elem)


def take_from_stack(stack_array: list):
    return stack_array.pop()


def postfix(aray: list):
    operations = ["+", "-", "*"]
    stack_array = []

    for elem in aray:
        if elem in operations:
            tmp_b = int(take_from_stack(stack_array))
            tmp_a = int(take_from_stack(stack_array))

            if elem == "+":
                tmp_answer = tmp_a + tmp_b
            elif elem == "-":
                tmp_answer = tmp_a - tmp_b
            else:
                tmp_answer = tmp_a * tmp_b


            put_to_stack(stack_array, tmp_answer)


        else:
            put_to_stack(stack_array, elem)
    return stack_array[0]


if __name__ == '__main__':

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    from lab4.utils import read_file_line, write_file

    array = read_file_line(path_input, 1).split()
    answer = postfix(array)
    write_file(path_output, str(answer))



