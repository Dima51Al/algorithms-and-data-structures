from lab2.utils import *


def max_delta(array: list) -> str:
    """формат array: дата(str), курс(float)"""
    string = ""
    date = [i[0] for i in array]
    course = [i[1] for i in array]
    pref_sum_course = [0]
    pref_sum_course += [course[i] + course[i + 1] for i in range(0, len(course) - 1)]
    maximum = 0
    for i in range(2, len(pref_sum_course)):
        tmp_min = min_max(pref_sum_course[1:i], 1)
        tmp_max = min_max(pref_sum_course[i:], -1)

        if tmp_max[0] - tmp_min[0] > maximum:
            maximum = tmp_max[0] - tmp_min[0]
            id_1 = tmp_min[1]
            id_2 = tmp_max[1]
            string = "купить " + date[id_1] + " продать " + date[id_2] + " получить " + str(maximum)
    return string


def main():
    array = []
    for i in open(path_input, "r", encoding="utf-8").readlines():
        array.append([i.split()[0], float(i.split()[1].replace(",", "."))])

    write_file(max_delta(array))


if __name__ == '__main__':
    main()