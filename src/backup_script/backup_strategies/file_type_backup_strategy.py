""" Strategy to copy the contents of a directory to a destination directory.

Created: 01.05.2021
@author: Max Weise
"""

import os
from shutil import copy

from backup_script.backup_strategies.abstract_backup_strategy import Backup


class FileTypeBackupStrategy(Backup):
    """ Copies files from a given source to a given destination.

    This class will copy only file types which have been specified.

    Attributes:
        source (str): Source directory from which to copy from.
        destination (str): Destination directory to which to copy to.
        fily_types (list[str]): All file types which should be copied.
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

    def set_file_types(self, new_file_types: list[str]) -> None:
        """ Sets the file_types attribute."""
        self.file_types = new_file_types

    def __check_for_relevant_files(self, lst: list[str]) -> list[str]:
        """ Search a given list of files for relevant filetypes."""
        return [f for f in lst if f.split('.')[-1] in self.file_types]

    def backup(self) -> None:
        """ Strategy method. Defines the backup strategie."""

        if not os.path.exists(self.source):
            raise ValueError('Source directory does not exist')

        if os.path.isfile(self.source):
            raise ValueError('Source directory can not be a file')

        for _, _, files in os.walk(self.source):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(os.path.join(self.source, f), self.destination)
