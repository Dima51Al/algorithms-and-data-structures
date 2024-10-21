def write_file(string: str) -> None:
    with open("output.txt", "w") as file:
        file.write(string)


def read_file() -> str:
    with open("input.txt", "r") as file:
        return file.read()
