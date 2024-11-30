import os
import shutil
import unittest


def remove_cache():
    cache_dirs = ['.pytest_cache', '__pycache__']
    cache_files = ['*.pyc', '*.pyo']

    for cache_dir in cache_dirs:
        for root, dirs, files in os.walk('.'):
            if cache_dir in dirs:
                dir_path = os.path.join(root, cache_dir)
                shutil.rmtree(dir_path)

    for cache_file in cache_files:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(tuple(cache_file.split('.'))):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)


def run_tests(start_dir):
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir=start_dir, pattern="*test_main.py")
    test_suite = unittest.TestSuite(tests)
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    runner.run(test_suite)


if __name__ == "__main__":
    remove_cache()
    run_tests("lab3")
