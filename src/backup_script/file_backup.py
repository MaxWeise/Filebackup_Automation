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
    """ Backup all files / directories in specified source
        dir to a specified destination.

        @params
            source:         str - source directory
            destination:    str - copy to destination
    """

    source: str
    destination: str

    def __init__(self, source: str = None, destination: str = None):
        """ Initialize File_Backup object by giving it a sourcedirectory to copy from and a destination to copy to."""

        if source:
            self.source = source

        if destination:
            self.destination = destination

    def backup(self) -> None:
        """ Copy recursivly from source to destination."""

        if not os.path.exists(self.source):
            raise ValueError('Source does not exist')

        if os.path.isfile(self.source):
            raise ValueError('Source can not be a file')

        copy_tree(self.source, self.destination)

    def __str__(self) -> str:
        return f'{type(self)}'

    def __repr__(self) -> str:
        """ Print a humanly readable representation to the console."""
        return(
            f'<{type(self)}> source: {self.source} | destination: {self.dest}'
        )

