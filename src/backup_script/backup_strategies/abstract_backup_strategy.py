""" Abstract strategy for the project.

Created: 20.07.2021
@author: Max Weise
"""

from abc import ABC, abstractmethod


class Backup(ABC):
    """ Copies files from a given source to a given destination.

    This is an abstract base definition which allows for the strategy-
    pattern to be used.

    Attributes:
        source (str): Source directory from which to copy from.
        destination (str): Destination directory to which to copy to.
    """
    source: str
    destination: str

    def set_source(self, source) -> None:
        """ Sets the source attribute of an instance"""
        self.source = source

    def set_destination(self, destination) -> None:
        """ Sets the destination attribute of an instance"""
        self.destination = destination

    @abstractmethod
    def backup(self) -> None:
        """ Copy recursivly from self.root to self.dest."""
        ...
