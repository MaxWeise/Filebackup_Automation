""" Testmodule for file_type_backup.py

created: 04.05.2021
author: Max Weise
"""

import os
import unittest
from unittest import TestCase

import backup_script.backup_strategies.file_type_backup_strategy as fts


class TestFileTypeBackupStrategy(TestCase):
    """ Test the Filebackupclass"""

    __SOURCE_PATH = 'test_source'
    __DESTIN_PATH = 'test_destin'
    __NUMBER_OF_FILES = 5

    def __check_for_correct_files(self, f: fts.FileTypeBackupStrategy) -> bool:
        """ Verifies that all copied files have the correct file extention."""

        files_in_dir = os.listdir(self.__DESTIN_PATH)
        all_files_correct = True

        for string in files_in_dir:
            file_extention = string.split('.')
            if file_extention[-1] not in self.f.file_types:
                all_files_correct = False

        return all_files_correct

    def setUp(self):
        """ Sets up the test environment."""

        if not os.path.exists(self.__SOURCE_PATH):
            os.makedirs(self.__SOURCE_PATH)

        if not os.path.exists(self.__DESTIN_PATH):
            os.makedirs(self.__DESTIN_PATH)

        # Write two sets of files with different file
        # extentions (.txt and .abcd)
        for i in range(self.__NUMBER_OF_FILES):
            file_path = os.path.join(self.__SOURCE_PATH, f'{str(i)}_name.txt')
            with open(file_path, 'w+'):    # Write empty files
                pass

        for i in range(self.__NUMBER_OF_FILES):
            file_path = os.path.join(self.__SOURCE_PATH, f'{str(i)}_name.abcd')
            with open(file_path, 'w+'):    # Write empty files
                pass

        self.f = fts.FileTypeBackupStrategy(
            self.__SOURCE_PATH,
            self.__DESTIN_PATH,
            None
        )

    def test_FileTypeBackup(self):  # sourcery skip: extract-duplicate-method
        """ Tests the main functionality of the class."""

        # First pass
        self.f.set_file_types(['txt'])
        self.f.backup()

        actual_num_of_files = len(os.listdir(self.__DESTIN_PATH))

        self.assertEqual(actual_num_of_files, self.__NUMBER_OF_FILES)
        self.assertTrue(self.__check_for_correct_files(self.f))

        # Second pass
        self.f.set_file_types(['abcd'])
        self.f.backup()

        actual_num_of_files = len(os.listdir(self.__DESTIN_PATH))
        self.assertEqual(actual_num_of_files, (2 * self.__NUMBER_OF_FILES))

    def test_FileTypeBackup_pathDoesNotExist(self):
        """ If a given path that does not exist, an error should be thrown."""

        self.f.set_source('does_not_exist')

        with self.assertRaises(ValueError):
            self.f.backup()

    def test_FileTypeBackup_pathIsFile(self):
        """ If a given path that is a file, an error should be thrown."""

        self.f.set_source(os.path.join(self.__SOURCE_PATH, '0' + '_name.abcd'))

        with self.assertRaises(ValueError):
            self.f.backup()

    def tearDown(self):
        """ Cleans the test env."""

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

