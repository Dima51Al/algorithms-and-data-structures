import os


class USA:
    dict_of_candidates = {}
    array_of_candidates = list()

    def is_candidate_exist(self, name):
        return name in self.array_of_candidates


    def add_candidate(self, name, voices):
        if self.is_candidate_exist(name):
            self.dict_of_candidates[name] += voices
        else:
            self.dict_of_candidates[name] = voices
            self.array_of_candidates.append(name)


    def info(self):
        answer = list()
        for name in self.array_of_candidates:
            answer.append(f"{name} {self.dict_of_candidates[name]}")
        return answer


if __name__ == '__main__':
    from lab6.utils import write_file, vertical_norm_view


    can_array = USA()
    answer_array = []

    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    def read_func(string: str):
        name = string.split()[0]
        voices = int(string.split()[1])
        can_array.add_candidate(name, voices)

    file = open(path_input, "r", encoding="utf-8").readlines()

    for string in file:
        read_func(string)

    answer_array = can_array.info()


    write_file(path_output, vertical_norm_view(answer_array))
