""" Module to copy a directory recursivly, either everything or only
    specific filetypes. In both cases, the structure of the directory
    will be keept.

Created: 15.02.2021
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
    """
    def __init__(self, source: str, destination: str):
        """ Initialize File_Backup object by giving it a
            rootdirectory to copy from and a destination
            to copy to.
        """
        self.source = source
        self.destination = destination

    def set_root(self, new_source: str) -> None:
        """ Set the root attribute of an instance."""
        self.source = new_source

    def set_dest(self, new_destination: str) -> None:
        """ Set the dest attribute of an instance."""
        self.destination = new_destination

    def backup(self) -> None:
        """ Copy recursivly from self.root to self.dest."""

        if not os.path.exists(self.source):
            raise ValueError('Root does not exist')

        if os.path.isfile(self.source):
            raise ValueError('Root can not be a file')

        copy_tree(self.source, self.destination)

    # def __str__(self) -> str:
    #     """ Print a humanly readable representation
    #         to the console.
    #     """
    #     return f'Backing up {self.root} into {self.dest}'

