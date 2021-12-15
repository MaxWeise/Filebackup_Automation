""" Define a text input dialog which asks the user which file extentions
    should be included in the copy procedure.

created 15.12.2021
@author Max Weise
"""

import tkinter as tk


class TextInputDialog:
    """ Display a GUI window to input file extentions."""

    # Attributes
    title: str
    file_extentions: list[str]

    def __init__(self, title: str = 'Header') -> None:
        self.title = title
        self.file_extentions = []

    def get_user_input(self) -> list[str]:
        """ Return the userinput as a list of strings."""
        return self.file_extentions

    def set_contents_input_dialog(self, input_text: str) -> None:
        """ Auxiliaray method to set the input of the dialog window."""
        pass

    def run(self) -> None:
        """ Run the mainloop to display the GUI window."""
        pass
