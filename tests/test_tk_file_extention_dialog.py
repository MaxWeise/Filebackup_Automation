#!/usr/bin/env python
""" Testsuite for the user text input

Created 15.12.2021
@author Max Weise
"""


import unittest
from unittest import TestCase

from backup_script.tk_file_extention_dialog import TextInputDialog


class Test_TextInputDialog(TestCase):
    """ Testcase for the custom tkinter text input dialog."""

    __UNDER_TEST: TextInputDialog

    def setUp(self) -> None:
        """ Setup an instance of the text input dialog."""
        self.__UNDER_TEST = TextInputDialog(title='Test Instance')

    def test_get_user_input(self) -> None:
        """ Test that the userinput is correct and gets returned as list of strings."""
        self.__UNDER_TEST.set_contents_input_dialog('Test Submit Button')    # Mock the userinput
        expected = ['Test', 'Submit', 'Button']

        self.__UNDER_TEST.run()
        actual = self.__UNDER_TEST.get_user_input()

        self.assertTrue(len(actual) > 0)
        self.assertEqual(len(actual), 3)
        self.assertAlmostEqual(actual.sort(), expected.sort())
        self.assertEqual(self.__UNDER_TEST.exit_code, 0)

    def test_cancle_button(self) -> None:
        """ Test the behaviour of the canlce button."""
        self.__UNDER_TEST.set_contents_input_dialog('Test Cancle Button')    # Mock the userinput
        expected = []

        self.__UNDER_TEST.run()
        actual = self.__UNDER_TEST.get_user_input()

        self.assertEqual(len(actual), 0)
        self.assertEqual(actual, expected)
        self.assertEqual(self.__UNDER_TEST.exit_code, 1)


if __name__ == '__main__':
    unittest.main()
