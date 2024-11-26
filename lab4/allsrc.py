import os
import subprocess


def run_all_src_files():
    for task in os.listdir(os.getcwd()):
        task_path = os.path.join(os.getcwd(), task)

        if os.path.isdir(task_path):
            src_dir = os.path.join(task_path, 'src')

            if os.path.isdir(src_dir):

                for root, dirs, files in os.walk(src_dir):
                    for file in files:
                        if file.endswith(".py") and file != "__init__.py":
                            file_path = os.path.join(root, file)
                            path_array = file_path.split("\\")
                            print('----------------------')
                            print(f"Launched {path_array[-3]}:")
                            subprocess.run(["python", file_path])
                            print('----------------------')


if __name__ == "__main__":
    run_all_src_files()

