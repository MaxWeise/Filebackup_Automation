""" Base class for a user interface.

Created: 11.04.2022
@author: Max Weise
"""


from typing import Protocol


class UI(Protocol):
    """ Base definition of a user interface.

    Provides basic methods for the user to interact with the programm.
    """

    def ask_source_directory(self) -> str:
        """ Returns a path to the source directoy."""
        raise NotImplementedError()

    def ask_destination_directory(self) -> str:
        """ Returns a path to the destination directoy."""
        raise NotImplementedError()

    def ask_file_types(self) -> list[str]:
        """ Returns a list of file types."""
        raise NotImplementedError()
