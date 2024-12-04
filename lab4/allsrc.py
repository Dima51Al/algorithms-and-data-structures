import os
import subprocess


def run_tasks():

    for task_folder in sorted(os.listdir(os.curdir)):
        src_path = os.path.join(task_folder, "src", "main.py")
        input_path = os.path.join(task_folder, "txtf", "input.txt")
        output_path = os.path.join(task_folder, "txtf", "output.txt")

        if os.path.isdir(task_folder) and os.path.exists(src_path):
            print("="*27)
            print(task_folder)
            print()


            if os.path.exists(input_path):
                with open(input_path, 'r') as file:
                    input_data = file.read()

                print(f"input.txt ({task_folder}):")
                print(input_data.strip())
            else:
                print("файл не найден.")
                continue

            subprocess.run(
                ["py", src_path]
            )



            if os.path.exists(output_path):
                with open(output_path, 'r') as file:
                    expected_output = file.read()
                print(f"output.txt ({task_folder}):")
                print(expected_output.strip())
            else:
                print(f"файл не найден.")


if __name__ == "__main__":
    run_tasks()
