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
            source:         str  - source directory
            destination:    str  - destination directory
            file_types:   list - filetyes to backup
    """

    source: str
    destination: str
    file_types: list[str]

    # TODO: Refactor the constructor to an empty one
    def __init__(self, source: str = None, destination: str = None, file_types: list = None):
        """ Initialize object by giving it source, destination
            and file types to copy.
        """
        if source:
            self.source = source

        if destination:
            self.destination = destination

        if file_types:
            self.file_types = file_types

    def get_source(self) -> str:
        """ Return the source attribute."""
        return self.source

    def get_dest(self) -> str:
        """ Get the contents of the __file_types attribute."""
        return self.destination

    def set_file_types(self, new_file_types: list) -> None:
        """ Set the attribute file_types to a specified list. Mostly used for testing."""
        self.file_types = new_file_types

    def get_file_types(self) -> list:
        """ Get the contents of the file_types attribute."""
        return self.file_types

    def __check_for_relevant_files(self, list_to_check: list) -> list:
        """ Search a given list of files for files with relevant filetypes."""
        return [f for f in list_to_check if f.split('.')[-1] in self.file_types]

    def backup(self) -> None:
        """ Copy specified files matching the sorting-criterium from source to destination."""

        if not os.path.exists(self.get_source()):
            raise ValueError('Source directory does not exist')

        if os.path.isfile(self.get_source()):
            raise ValueError('Source directory can not be a file')

        for _, _, files in os.walk(self.get_source()):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(os.path.join(self.get_source(), f), self.get_dest())

    def __str__(self) -> str:
        """ Print a humanly readable representation to the console."""
        return(
            f'<{type(self)}> source: {self.source} | destination: {self.dest} | types: {self.file_types}'
        )
