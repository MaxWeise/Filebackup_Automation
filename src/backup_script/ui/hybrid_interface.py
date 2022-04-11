""" Hybrid interface for the project.

Implement methods to interact with the user via the cli
and gui.

Created: 11.04.2022
@author: Max Weise
"""


from tkinter import Tk, filedialog


class HybridInterface:
    """ Hybrid implementation of a user interface.

    Methods get implemented by using the CLI and a GUI.
    This class is a "quick and dirty" implementation of an actuall UI.
    If more time and knowledge is at available, dedicated graphical and CL
    interfaces will be implemented.
    """

    def __init__(self):
        self.root = Tk()
        # Don't show a tk window when runing the programm
        self.root.withdraw()

    def ask_source_directory(self) -> str:
        """ Returns a path to the source directoy."""
        return filedialog.askdirectory(
            parent=self.root,
            title='Please select a source directory'
        )

    def ask_destination_directory(self) -> str:
        """ Returns a path to the destination directoy."""
        return filedialog.askdirectory(
            parent=self.root,
            title='Please select a destination directory'
        )

    def ask_file_types(self) -> list[str]:
        """ Returns a list of file types."""
        user_in = input(
            'Plase input the fileextentions you want to backup.'
            '\nThe input should only contain letters and be separated by '
            'one space.'
        )

        return user_in.split(' ')
