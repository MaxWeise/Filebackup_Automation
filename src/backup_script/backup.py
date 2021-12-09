""" Abstract baseclass for filebackup and file_type_backup

Created: 20.07.2021
@author: Max Weise
"""

from abc import ABC, abstractmethod


class Backup(ABC):
    """ Define an abstract base class for the other procedures

        @params
            root: str - root directory
            destination: str - copy to destination
    """

    @abstractmethod
    def backup(self) -> None:
        """ Copy recursivly from self.root to self.dest."""

    @abstractmethod
    def __str__(self) -> str:
        """ Print a humanly readable representation
            to the console.
        """
