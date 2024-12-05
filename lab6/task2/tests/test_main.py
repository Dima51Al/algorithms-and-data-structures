import unittest
from lab6.task2.src.main import PhoneBook
from lab6.utils import *


class PostfixTestCase(unittest.TestCase):

    def test_should_phonebook_add_max_values(self):
        # given
        difficulty = 10**5
        phonebook = PhoneBook()


        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            phonebook.add(10 ** 7 - i - 1, "Dima")


        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 6)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_phonebook_remove_max_values(self):
        # given
        difficulty = 10 ** 5
        phonebook = PhoneBook()
        for i in range(difficulty):
            phonebook.add(10 ** 7 - i - 1, "Dima")

        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            phonebook.delete_from_number(10 ** 7 - i - 1)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 6)
        self.assertLessEqual(final_memory - start_memory, 512)

    def test_should_phonebook_check_from_number(self):
        # given
        difficulty = 10 ** 5
        phonebook = PhoneBook()
        for i in range(difficulty):
            phonebook.add(10 ** 7 - i - 1, "Dima")

        # when
        start_memory, start_time = memory_and_time()

        for i in range(difficulty):
            phonebook.find_from_number(10 ** 7 - i - 1)

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 6)
        self.assertLessEqual(final_memory - start_memory, 512)


if __name__ == '__main__':
    unittest.main()
