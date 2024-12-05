import os


class PhoneBook:
    array = [None] * (10 ** 7)

    def add(self, number, name):
        self.array[number] = name


    def delete_from_number(self, number: int):
        self.array[number] = None

    def find_from_number(self, number):
        answer = self.array[number]
        if answer is None:
            return "not found"
        return answer


if __name__ == '__main__':
    phonebook_array = PhoneBook()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')


    def read_func(string: str):
        if "add" in string:
            number = int(string.split()[1])
            name = string.split()[2]
            phonebook_array.add(number, name)

        elif "del" in string:
            number = int(string.split()[1])
            phonebook_array.delete_from_number(number)

        elif "find" in string:
            number = int(string.split()[1])
            answer = answer_array.append(phonebook_array.find_from_number(number))
            return answer




    from lab6.utils import read_file_line, write_file, vertical_norm_view

    count_of_strings = int(read_file_line(path_input, 0))

    for i in range(count_of_strings):
        read_func(read_file_line(path_input, i + 1))

    write_file(path_output, vertical_norm_view(answer_array))
