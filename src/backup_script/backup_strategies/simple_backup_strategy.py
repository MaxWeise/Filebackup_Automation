""" Module to copy a directory recursivly, either everything or only
    specific filetypes. In both cases, the structure of the directory
    will be keept.

Created: 15.02.2021
@author: Max Weise
"""

import os
from distutils.dir_util import copy_tree

from backup_script.backup_strategies.abstract_backup_strategy import Backup


class SimpleBackupStrategy(Backup):
    """ Copies all contents from a given source to a given destination."""

    source: str
    destination: str

    def __init__(self, source: str = None, destination: str = None):
        """ Initializes File_Backup object."""
        self.source = source
        self.destination = destination

    def backup(self) -> None:
        """ Copy recursivly from source to destination."""

        if not os.path.exists(self.source):
            raise ValueError('Source does not exist')

        if os.path.isfile(self.source):
            raise ValueError('Source can not be a file')

        copy_tree(self.source, self.destination)
