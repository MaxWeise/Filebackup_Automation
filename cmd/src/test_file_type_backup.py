""" Testmodule for file_type_backup.py

created: 04.05.2021
last revision: 04.05.2021
author: Max Weise
"""

# NOTE: Naming convention, <> = Identifier, [] = Optional Description - If empty, test for 'normal' run
# For Classes: Test<Name>(TestCase)
# For Methods: def test_<nameInCamelCase>_[ExpectedConditions](self)

# Execute using $ python -m unittest -v test_module.TestClass.test_method    

import os
import unittest

from unittest import TestCase
from file_type_backup import File_Type_Backup

class TestFile_Type_Backup(TestCase):
    """ Test the Filebackupclass

        @author
            Max Weise
    """

    __SOURCE_PATH = 'test_source' 
    __DESTIN_PATH = 'test_destin'
    __NUMBER_OF_FILES = 5
    
    def setUp(self):
        """ Create the directories and files needed for the test. Create an instance of File_Type_Backup"""
        if not os.path.exists(self.__SOURCE_PATH):
            os.makedirs(self.__SOURCE_PATH)

        if not os.path.exists(self.__DESTIN_PATH):
            os.makedirs(self.__DESTIN_PATH)

        # Write two sets of files with different file extentions (.txt and .abcd)
        for i in range(self.__NUMBER_OF_FILES):
            file_path = os.path.join(self.__SOURCE_PATH, str(i) + '_name.txt')
            with open(file_path, 'w+') as f:    # Write empty files
                pass

        for i in range(self.__NUMBER_OF_FILES):
            file_path = os.path.join(self.__SOURCE_PATH, str(i) + '_name.abcd')
            with open(file_path, 'w+') as f:    # Write empty files
                pass

        self.f = File_Type_Backup(self.__SOURCE_PATH, self.__DESTIN_PATH)
    
    def test_FileTypeBackup(self):
        """ Test the main functionality of the class by copying all specified files to the intended directory."""
        # We do two passes: 
        # First: get all .txt files, then assert len(__DESTIN_PATH) = __NUMBER_OF_FILES
        # Second: get all .abcd files, then assert len(__DESTIN_PATH) = 2 * __NUMBER_OF_FILES

        # First pass
        self.f.set_file_types(['txt'])
        self.f.backup_file_types()

        self.assertEqual(len(os.listdir(self.__DESTIN_PATH)), self.__NUMBER_OF_FILES)
        
        # Second pass
        self.f.set_file_types(['abcd'])
        self.f.backup_file_types()

        self.assertEqual(len(os.listdir(self.__DESTIN_PATH)), (2 * self.__NUMBER_OF_FILES))

    def tearDown(self):
        """ Remove all files and directories used in the testing process. Remove the File_Type instance."""
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

