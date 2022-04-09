""" Testmodule for file_backup.py

created: 28.04.2021
author: Max Weise
"""

import os
import unittest
from unittest import TestCase

import backup_script.backup_strategies.simple_backup_strategy as sbs


class TestFile_Backup(TestCase):
    """ Test the Filebackupclass"""

    __SOURCE_PATH = 'test_source'
    __DESTIN_PATH = 'test_destin'
    __NUMBER_OF_FILES = 5

    def setUp(self):
        """ Creates the directories and files needed for the test. """

        if not os.path.exists(self.__SOURCE_PATH):
            os.makedirs(self.__SOURCE_PATH)

        if not os.path.exists(self.__DESTIN_PATH):
            os.makedirs(self.__DESTIN_PATH)

        for i in range(self.__NUMBER_OF_FILES):
            file_path = os.path.join(self.__SOURCE_PATH, f'{str(i)}_name.txt')
            with open(file_path, 'w+'):
                pass

        self.f = sbs.SimpleBackupStrategy(
            self.__SOURCE_PATH,
            self.__DESTIN_PATH
        )

    def test_fileBackup(self):
        """ Tests if all files in self.SOURCE_PATH get copied correctly."""
        self.f.backup()

        actual_file_number = len(os.listdir(self.__DESTIN_PATH))
        self.assertEqual(actual_file_number, self.__NUMBER_OF_FILES)

    def test_fileBackup_pathDoesNotExist(self):
        """ Raise an error if the source path given does not exist."""

        self.f.set_source('does_not_exist')

        with self.assertRaises(ValueError):
            self.f.backup()

    def test_fileBackup_pathIsFile(self):
        self.f.set_source(os.path.join(self.__SOURCE_PATH, '0_name.txt'))

        with self.assertRaises(ValueError):
            self.f.backup()

    def tearDown(self):
        """ Cleans up test environment."""

        if os.path.isdir(self.__SOURCE_PATH):
            source_files = os.listdir(self.__SOURCE_PATH)

            for f in source_files:
                os.remove(os.path.join(self.__SOURCE_PATH, f))

        if os.path.isdir(self.__DESTIN_PATH):
            destin_files = os.listdir(self.__DESTIN_PATH)

            for f in destin_files:
                os.remove(os.path.join(self.__DESTIN_PATH, f))

        os.rmdir(self.__SOURCE_PATH)
        os.rmdir(self.__DESTIN_PATH)

        del self.f


if __name__ == '__main__':
    unittest.main()
