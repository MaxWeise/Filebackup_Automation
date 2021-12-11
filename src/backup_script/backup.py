""" Abstract baseclass for file_backup and file_type_backup

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

    source: str
    destination: str

    # TODO: Implement the setters, so instances of both subclasses can use them
    def set_source(self, source) -> None:
        """ Set the source attribute of an instance"""
        self.source = source

    def set_destination(self, destination) -> None:
        """ Set the destination attribute of an instance"""
        self.destination = destination

    @abstractmethod
    def backup(self) -> None:
        """ Copy recursivly from self.root to self.dest."""
