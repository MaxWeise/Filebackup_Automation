""" Testmodule for file_backup_classes.py

created: 28.04.2021
last revision: 01.05.2021
author: Max Weise
"""

# NOTE: Naming convention, <> = Identifier, [] = Optional Description
# For Classes: Test<Name>(TestCase)
# For Methods: def test_<nameInCamelCase>_[ExpectedConditions](self)

# setUp() runs before the test method executes
# tearDown() after it has been executed

# Execute using $ python -m unittest -v test_module.TestClass.test_method    

import os
import unittest

from unittest import TestCase
from file_backup_classes import File_Backup


class TestFile_Backup(TestCase):
    """ Test the Filebackupclass

        @author
            Max Weise
    """

    __SOURCE_PATH = 'test_source' 
    __DESTIN_PATH = 'test_destin'
    __number_of_files = 5
    
    def setUp(self):
        """ Create the directories and files needed for the test. Create an instance of File_Backup"""
        if not os.path.exists(self.__SOURCE_PATH):
            os.makedirs(self.__SOURCE_PATH)

        if not os.path.exists(self.__DESTIN_PATH):
            os.makedirs(self.__DESTIN_PATH)

        for i in range(self.__number_of_files):
            file_path = os.path.join(self.__SOURCE_PATH, str(i) + '_name.txt')
            with open(file_path, 'w+') as f:    # Write empty files
                pass

        self.f = File_Backup(self.__SOURCE_PATH, self.__DESTIN_PATH)
    
    def test_fileBackup_BackupTree(self):
        """ Test if all files in self.SOURCE_PATH get copied correctly."""
        self.f.backup_tree()

        self.assertEqual(len(os.listdir(self.__DESTIN_PATH)), self.__number_of_files)
        
    def tearDown(self):
        """ Remove all files and directories used in the testing process. Remove the File_Backup instance."""
        source_files = os.listdir(self.__SOURCE_PATH)
        destin_files = os.listdir(self.__DESTIN_PATH)

        for f in source_files:
            os.remove(os.path.join(self.__SOURCE_PATH, f))

        for f in destin_files:
            os.remove(os.path.join(self.__DESTIN_PATH, f))
        
        os.rmdir(self.__SOURCE_PATH)
        os.rmdir(self.__DESTIN_PATH)

        del self.f

if __name__ == '__main__':
    unittest.main()
