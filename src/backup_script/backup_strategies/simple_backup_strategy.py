""" Strategy to copy files recursivly by type.

Created: 15.02.2021
@author: Max Weise
"""

import os
# from distutils.dir_util import copy_tree
import shutil
from backup_script.backup_strategies.abstract_backup_strategy import Backup


class SimpleBackupStrategy(Backup):
    """ Copies files from a given source to a given destination.

    Attributes:
        source (str): Source directory from which to copy from.
        destination (str): Destination directory to which to copy to.
    """
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

        shutil.copytree(self.source, self.destination, dirs_exist_ok=True)
