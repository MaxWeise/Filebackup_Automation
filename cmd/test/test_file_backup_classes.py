""" Testmodule for file_backup_classes.py

created: 28.04.2021
last revision: 29.04.2021
author: Max Weise
"""

# NOTE: Naming convention, <> = Identifier, [] = Optional Description
# For Classes: Test<Name>(TestCase)
# For Methods: def test_<nameInCamelCase>_[ExpectedConditions](self)

# setUp() runs before the test method executes
# tearDown() after it has been executed

# Execute using $ python -m unittest -v test_module.TestClass.test_method    


import unittest
import os
import shutil
from unittest import TestCase

class TestFile_Backup(TestCase):
    """ Test the Filebackupclass

        @author
            Max Weise
    """

    def setUp(self):
        """ Create the directories and files needed for the test."""
        SOURCE_PATH = 'test_source' 
        DESTIN_PATH = 'test_destin'

        # For some reason, mkdir throws a wrong 'fileExistsError'
        os.makedirs(SOURCE_PATH, exist_ok=True)
        os.makedirs(DESTIN_PATH, exist_ok=True)

        for i in range(5):
            file_path = os.path.join(SOURCE_PATH, str(i) + '_name.txt')
            with open(file_path, 'w+') as f:
                pass

    def test_backupTree(self):
        pass

    def tearDown(self):
        """ Remove the created test directories."""
        #! Throws an error on rmtree. Dirs get removed correctly but test is marked as failed
        SOURCE_PATH = 'test_source' 
        DESTIN_PATH = 'test_destin'

        shutil.rmtree(SOURCE_PATH)
        shutil.rmtree(DESTIN_PATH)
        

if __name__ == '__main__':
    unittest.main()