import os


def create_lab_structure(N, array):
    lab_dir = f"lab{N}"
    os.makedirs(lab_dir, exist_ok=True)

    for task_num in array:
        task_dir = os.path.join(lab_dir, f"task{task_num}")
        os.makedirs(task_dir, exist_ok=True)

        src_dir = os.path.join(task_dir, "src")
        tests_dir = os.path.join(task_dir, "tests")
        txtf_dir = os.path.join(task_dir, "txtf")

        os.makedirs(src_dir, exist_ok=True)
        os.makedirs(tests_dir, exist_ok=True)
        os.makedirs(txtf_dir, exist_ok=True)

        with open(os.path.join(task_dir, "README.MD"), "w", encoding="utf-8") as f:
            f.write(f"# Задание {task_num}\n")

        with open(os.path.join(src_dir, "main.py"), "w") as f:
            f.write("")

        with open(os.path.join(tests_dir, "test.py"), "w") as f:
            f.write("")

        with open(os.path.join(txtf_dir, "input.txt"), "w") as f:
            f.write("")

        with open(os.path.join(txtf_dir, "output.txt"), "w") as f:
            f.write("")

    print(f"Структура для лабораторной работы {N} успешно создана.")


if __name__ == '__main__':
    N = 4
    array = [2, 3, 6, 8, 13, 7]
    inp = input(f"Создание {array}, Напишите абракадабра: ")
    if inp == "абракадабра":
        create_lab_structure(N, array)
