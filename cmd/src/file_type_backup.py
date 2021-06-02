""" Class to backup specified filetypes

Created: 01.05.2021
Last revision: 02.06.2021
@author: Max Weise
"""
import os

from shutil import copy

from .file_backup import File_Backup


class File_Type_Backup(File_Backup):
    """ This class can be used to backup files regarding
        their types (file endings '.xxx').

        @params
            root:         str  - root directory
            destination:  str  - destination directory
            __file_types: list - filetyes to backup

        @author
            Max Weise
    """

    def __init__(self, root: str, destination: str, file_types: list):
        """ Initialize object by giving it root, destination
            and file types to copy.
        """
        super().__init__(root, destination)
        self.__file_types = file_types

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
        return_list = []
        for f in list_to_check:
            if f.split('.')[-1] in self.__file_types:
                return_list.append(f)

        return return_list

    def backup_file_types(self) -> None:
        """ Copy specified files matching the sorting-criterium
            from root to destination.
        """

        if not os.path.exists(self.root):
            raise ValueError('Root does not exist')

        if os.path.isfile(self.root):
            raise ValueError('Root can not be a file')

        for root, dirs, files in os.walk(self.root):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(os.path.join(root, f), self.dest)



