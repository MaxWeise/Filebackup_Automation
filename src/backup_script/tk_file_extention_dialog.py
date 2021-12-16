""" Define a text input dialog which asks the user which file extentions
    should be included in the copy procedure.

created 15.12.2021
@author Max Weise
"""

import tkinter as tk
from tkinter.constants import END


class TextInputDialog:
    """ Display a GUI window to input file extentions."""

    # Attributes
    exit_code: int
    file_extentions: list[str]

    __EXIT_CODES: dict[str, int] = {
        'NOTRUN' : -1,
        'SUCCESS' : 0,
        'ERROR' : 1,
    }

    def __init__(self, title: str = 'Header') -> None:
        self.root = tk.Tk()
        self.root.title(title)
        # self._setup_gui(self.root)

        self.file_extentions = []
        self.exit_code = self.__EXIT_CODES['NOTRUN']

    # def _setup_gui(self, tk_root) -> None:
    #     """ Setup the tkinter GUI."""
        self.root.geometry('200x100')
        self.root.config(bg='skyblue')    # Color of root window

        tk.Label(self.root, text='Input File Extentions').pack(side=tk.TOP, padx=5, pady=5)

        self.text_input_label = tk.Entry(self.root)
        self.text_input_label.pack(padx=5, pady=5)

        # Submit the userinput
        submit_button = tk.Button(self.root, text='Submit', command=self._click_submit_buttton)
        submit_button.pack(side=tk.RIGHT, padx=20, pady=5)

        # Cancle the userinput
        cancle_button = tk.Button(self.root, text='Cancle', command=self._click_cancle_buttton)
        cancle_button.pack(side=tk.LEFT, padx=20, pady=5)

    def _click_submit_buttton(self) -> None:
        """ This method will execute when the user clicks the submit button on the GUI
            It will safe the contents from the textfield as a list
        """
        self.file_extentions = self.text_input_label.get().split(' ')
        self.exit_code = self.__EXIT_CODES['SUCCESS']
        self.root.quit()

    def _click_cancle_buttton(self) -> None:
        """ This method will execute when the user clicks the cancle button on the GUI
            It will clear the contents of the textfield.
        """
        self.file_extentions = []   # Explicitly setting the list to an empty one
        self.exit_code = self.__EXIT_CODES['ERROR']
        self.root.quit()

    def get_user_input(self) -> list[str]:
        """ Return the userinput as a list of strings."""
        return self.file_extentions

    def set_contents_input_dialog(self, input_text: str) -> None:
        """ Auxiliaray method to set the input of the dialog window."""
        self.text_input_label.insert(END, input_text)

    def run(self) -> None:
        """ Run the mainloop to display the GUI window."""
        self.root.mainloop()
