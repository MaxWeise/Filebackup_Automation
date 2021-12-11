""" Class to backup specified filetypes

Created: 01.05.2021
@author: Max Weise
"""
import os

from shutil import copy

from backup_script.backup import Backup


class File_Type_Backup(Backup):
    """ This class can be used to backup files regarding
        their types (file endings '.xxx').

        @params
            root:         str  - root directory
            destination:  str  - destination directory
            __file_types: list - filetyes to backup
    """

    def __init__(self, source: str, destination: str, file_types: list):
        """ Initialize object by giving it root, destination
            and file types to copy.
        """
        self.__source = source
        self.__destination = destination
        self.__file_types = file_types

    def set_root(self, new_source: str) -> None:
        """ Set the root attribute to a new root."""
        self.__source = new_source

    def get_root(self) -> str:
        """ Return the root attribute."""
        return self.__source

    def set_dest(self, new_destination: str) -> None:
        """ Set the dest attribute to a new dest."""
        self.__destination = new_destination

    def get_dest(self) -> str:
        """ Get the contents of the __file_types attribute."""
        return self.__destination

    def set__file_types(self, new_file_types: list) -> None:
        """ Set the attribute __file_types to a specified list.
            Mostly used for testing.
        """
        self.__file_types = new_file_types

    def get__file_types(self) -> list:
        """ Get the contents of the __file_types attribute."""
        return self.__file_types

    def __check_for_relevant_files(self, list_to_check: list) -> list:
        """ Search a given list of files for files with relevant
            filetypes.
        """
        return [f for f in list_to_check if f.split('.')[-1] in self.__file_types]

    def backup(self) -> None:
        """ Copy specified files matching the sorting-criterium from root to destination."""

        if not os.path.exists(self.get_root()):
            raise ValueError('Root does not exist')

        if os.path.isfile(self.get_root()):
            raise ValueError('Root can not be a file')

        for _, _, files in os.walk(self.get_root()):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(os.path.join(self.get_root(), f), self.get_dest())

    # def __str__(self) -> str:
    #     """ Print a humanly readable representation to the console."""
    #     return f'Backing up {self.root} into {self.dest} using {self.__file_types}'
