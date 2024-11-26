import unittest
from lab4.task3.src.main import is_right_bracket_sequence
from lab4.utils import *


class BracketSequenceTestCase(unittest.TestCase):

    def test_should_check_is_right_bracket_sequence(self):
        # given

        test_for_true = [
            "()()",
            "[]{}[()]",
            "{}",
            "([])",
            "[{()}]",
            "{{[[(())]]}}",
            "(()(()))",
            "[{()}]([]{})",
            "([{}])",
            "((((()))))",
            "[](){}",
            "{[()()][]}",
            "[([]){}]",
            "{()}",
            "[{()}]",
            "({[({[]})]})",
            "([]{})",
            "()[[]]{{}}",
            "[{[()()]()}]",
            "(([]){})"
        ]

        test_for_false = [
            "{(",
            "{}{()]",
            "[}",
            "[[",
            "({[)]})",
            "(()",
            "{{[[(())]}",
            "([)]",
            "[(])",
            "{[(])}",
            "[(])}",
            "([{})]",
            "[({)]",
            "((",
            "((]",
            "{[()]})]",
            "[({})](]",
            "[{()}]{[}]",
            "{{[[(())]]}})",
            "{[()]}}"
        ]

        # when
        start_memory, start_time = memory_and_time()



        for elem in test_for_true:
            self.assertTrue(is_right_bracket_sequence(elem))
        for elem in test_for_false:
            self.assertFalse(is_right_bracket_sequence(elem))

        final_memory, final_time = memory_and_time()

        # then
        self.assertLessEqual(final_time - start_time, 2)
        self.assertLessEqual(final_memory - start_memory, 256)


if __name__ == '__main__':
    unittest.main()
