import time

import memory_profiler


def write_file(path: str, string: str) -> None:
    with open(path, "w") as file:
        file.write(string)


def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


def read_file_line(path: str, num: int) -> str:
    line = open(path, "r").readlines()[num]
    return line


def test_base(function, first, second):
    memory_before = memory_profiler.memory_usage()[0]

    tmp = time.time()
    function(first, second)
    tmp = time.time() - tmp

    memory_after = memory_profiler.memory_usage()[0]

    print()
    print("Время выполнения: ", tmp)
    print("Использование памяти: ", memory_after - memory_before, "МБ")
