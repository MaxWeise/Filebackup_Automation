""" Class to backup specified filetypes

Created: 01.05.2021
@author: Max Weise
"""
import os
from shutil import copy

from backup_script.backup import Backup


class BackupFileTypeStrategie(Backup):
    """ Copies files from a given source to a given destination.

    This strategy selects the files to be copied by their file extention.
    """

    source: str
    destination: str
    file_types: list[str]

    def __init__(
        self,
        source: str = None,
        destination: str = None,
        file_types: list[str] = None
    ):
        self.source = source
        self.destination = destination
        self.file_types = file_types

    def get_source(self) -> str:
        """ The source attribute."""
        return self.source

    def get_dest(self) -> str:
        """ The destination attribute."""
        return self.destination

    def set_file_types(self, new_file_types: list[str]) -> None:
        """ Sets the file_types attribute."""
        self.file_types = new_file_types

    def get_file_types(self) -> list:
        """ Get the contents of the file_types attribute."""
        return self.file_types

    def __check_for_relevant_files(self, lst: list[str]) -> list[str]:
        """ Search a given list of files for relevant filetypes."""
        return [f for f in lst if f.split('.')[-1] in self.file_types]

    def backup(self) -> None:
        """ Strategy method. Defines the backup strategie."""

        if not os.path.exists(self.get_source()):
            raise ValueError('Source directory does not exist')

        if os.path.isfile(self.get_source()):
            raise ValueError('Source directory can not be a file')

        for _, _, files in os.walk(self.get_source()):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(os.path.join(self.get_source(), f), self.get_dest())
