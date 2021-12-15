""" Define a text input dialog which asks the user which file extentions
    should be included in the copy procedure.

created 15.12.2021
@author Max Weise
"""

import tkinter as tk


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
        self._setup_gui(self.root)

        self.file_extentions = []
        self.exit_code = self.__EXIT_CODES['NOTRUN']

    def _setup_gui(self, tk_root) -> None:
        """ Setup the tkinter GUI."""
        tk_root.geometry('200x100')
        tk_root.config(bg='skyblue')    # Color of root window

        tk.Label(tk_root, text='Input Fily Extentions').pack(side=tk.TOP, padx=5, pady=5)

        text_input_label = tk.Entry(tk_root)
        text_input_label.pack(padx=5, pady=5)

        # Submit the userinput
        submit_button = tk.Button(tk_root, text='Submit')
        submit_button.pack(side=tk.RIGHT, padx=20, pady=5)

        # Cancle the userinput
        cancle_button = tk.Button(tk_root, text='Cancle')
        cancle_button.pack(side=tk.LEFT, padx=20, pady=5)

    def get_user_input(self) -> list[str]:
        """ Return the userinput as a list of strings."""
        return self.file_extentions

    def set_contents_input_dialog(self, input_text: str) -> None:
        """ Auxiliaray method to set the input of the dialog window."""
        pass

    def run(self) -> None:
        """ Run the mainloop to display the GUI window."""
        # self.root.withdraw()
        try:
            self.root.mainloop()
        except Exception as e:
            self.root.quit()
            print(e)

    def exit_on_cancle(self) -> None:
        """ Clear the userinput and set exitcode to 1 when user clicks on cacle."""
        pass

    def safe_user_input(self) -> None:
        """ Safe the userinput and set exit code to 0."""
        pass
