""" Testmodule for main.py

created: 03.06.2021
last revision: 03.06.2021
author: Max Weise
"""

import os, unittest, sys

from unittest import TestCase

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.main import main


class Test_Main(TestCase):

    def setUp(self):
        """ Setup all neccessary files."""
        pass

    def test_file_backup(self):
        """ Test the file backup procedure."""
        pass

    def test_file_type_backup(self):
        """ Test the file type backup procedure."""
        pass

    def test_single_file_backup(self):
        """ Test the single file backup procedure."""
        pass

    def tearDown(self):
        """ Clean up any remaining directories after tests."""
        pass
