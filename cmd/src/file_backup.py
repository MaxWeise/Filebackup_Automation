""" Module to copy a directory recursivly, either everything or only
    specific filetypes. In both cases, the structure of the directory
    will be keept.

Created: 15.02.2021
Last revision: 28.05.2021
@author: Max Weise
"""

import os
from distutils.dir_util import copy_tree

from .backup import Backup


class File_Backup(Backup):
    """ Backup all files / directories in specified root
        dir to a specified destination.

        @params
            root: str - root directory
            destination: str - copy to destination

        @author
            Max Weise
    """ 
    def __init__(self, root: str, destination: str):
        """Initialize File_Backup object by giving it a
            rootdirectory to copy from and a destination
            to copy to.
        """
        self.root = root
        self.dest = destination

    def set_root(self, new_root: str) -> None:
        """ Set the root attribute of an instance."""
        self.root = new_root

    def set_dest(self, new_dest: str) -> None:
        """ Set the dest attribute of an instance."""
        self.dest = new_dest

    def backup(self) -> None:
        """Copy recursivly from self.root to self.dest."""

        if not os.path.exists(self.root):
            raise ValueError('Root does not exist')

        if os.path.isfile(self.root):
            raise ValueError('Root can not be a file')

        copy_tree(self.root, self.dest)

    def __str__(self) -> str:
        """Print a humanly readable representation
            to the console.
        """
        return f'Backing up {self.root} into {self.dest}'

