import os
import sys
import subprocess


def run_tasks():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    for task_folder in sorted(os.listdir(base_dir)):
        abs_path = os.path.join(base_dir, task_folder)
        src_path = os.path.join(abs_path, "src", "main.py")
        input_path = os.path.join(abs_path, "txtf", "input.txt")
        output_path = os.path.join(abs_path, "txtf", "output.txt")



        if os.path.isdir(abs_path) and os.path.isfile(src_path) and src_path.endswith(".py"):
            print("=" * 27)
            print(task_folder)
            print()

            if os.path.exists(input_path):
                with open(input_path, 'r') as file:
                    input_data = file.read()
                print(f"input.txt ({task_folder}):")
                print(input_data.strip())
            else:
                print(f"error: {input_path}")

            subprocess.run(
                ["py", src_path],
                cwd=project_root,
                env={**os.environ, "PYTHONPATH": project_root}

            )


            if os.path.exists(output_path):
                with open(output_path, 'r') as file:
                    expected_output = file.read()
                print(f"output.txt ({task_folder}):")
                print(expected_output.strip())
            else:
                print(f"error: {output_path}")


if __name__ == "__main__":
    run_tasks()
