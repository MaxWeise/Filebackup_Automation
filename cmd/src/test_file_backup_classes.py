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
from .. import src

class TestFile_Backup(TestCase):
    """ Test the Filebackupclass

        @author
            Max Weise
    """

    SOURCE_PATH = 'test_source' 
    DESTIN_PATH = 'test_destin'
    number_of_files = 5
    
    def setUp(self):
        """ Create the directories and files needed for the test."""
        print('Running setUp')
        if not os.path.exists(self.SOURCE_PATH):
            os.makedirs(self.SOURCE_PATH)

        if not os.path.exists(self.DESTIN_PATH):
            os.makedirs(self.DESTIN_PATH)

        for i in range(self.number_of_files):
            file_path = os.path.join(self.SOURCE_PATH, str(i) + '_name.txt')
            with open(file_path, 'w+') as f:    # Write empty files
                pass
    
    def test_fileBackup_BackupTree(self):
        """ Test if all files in self.SOURCE_PATH get copied correctly."""
        f = File_Backup(self.SOURCE_PATH, self.DESTIN_PATH)
        f.backup_tree()

        self.assertEqual(len(os.listdir(self.DESTIN_PATH)), self.number_of_files)
        
    def tearDown(self):
        """ Remove all files and directories used in the testing process."""
        print('Running tearDown')
        source_files = os.listdir(self.SOURCE_PATH)
        destin_files = os.listdir(self.DESTIN_PATH)

        for f in source_files:
            os.remove(os.path.join(self.SOURCE_PATH, f))

        for f in destin_files:
            os.remove(os.path.join(self.DESTIN_PATH, f))
        
        os.rmdir(self.SOURCE_PATH)
        os.rmdir(self.DESTIN_PATH)

if __name__ == '__main__':
    unittest.main()
