import os


def is_right_bracket_sequence(string: str) -> bool:
    """ string must contain only []{}()"""


    bracket_dict = {
        "[": "]",
        "{": "}",
        "(": ")"
    }

    if len(string) == 0:
        return True

    if len(string) == 2:
        return string in ["()", "[]", "{}"]

    if len(string) % 2 == 1:
        return False

    start = string[0]

    if start in ")}]":

        return False

    finish = bracket_dict[start]
    repeats = 0
    for i in range(len(string)):
        if string[i] == start:
            repeats += 1

        if string[i] == finish:
            repeats -= 1
            if repeats == 0:
                A = is_right_bracket_sequence(string[1:i])
                B = is_right_bracket_sequence(string[i+1:])
                return A and B

    return False






if __name__ == '__main__':

    def correct_answer(value):
        if value:
            return "YES"
        return "NO"

    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')



    from lab4.utils import read_file_line, write_file, vertical_norm_view

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        tmp_string = read_file_line(path_input, i+1)
        tmp_answer = is_right_bracket_sequence(str(tmp_string))
        answer_array.append(correct_answer(tmp_answer))

    write_file(path_output, vertical_norm_view(answer_array))


