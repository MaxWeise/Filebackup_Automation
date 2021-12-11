#!/usr/bin/env python
""" Automatically backup files

Created on: 27.01.2021
@author: Max Weise
"""

import argparse
import tkinter as tk

from backup_script.backup import Backup
from backup_script.file_backup import File_Backup
from backup_script.file_type_backup import File_Type_Backup


PROCEDURES = {
    'simple_backup' : File_Backup(),
    'file_type_backup' : File_Type_Backup(),
}


def _get_userinput_filetypes() -> list[str]:
    """ Open a textinput box to the user and
        return a list of entries
    """
    # TODO: This is bad practice. Research a better way of doing this and rework this mechanism (1)
    global return_val
    return_val = []

    master = tk.Tk()
    tk.Label(master, text="First Name").grid(row=0)

    e1 = tk.Entry(master)

    e1.grid(row=0, column=1)

    # TODO: This belongs to (1)
    def set_return_to_none() -> None:
        global return_val
        return_val = []
        master.quit()

    def set_return_to_list() -> None:
        global return_val
        return_val = e1.get().split(' ')
        master.quit()

    tk.Button(
        master,
        text='Quit',
        command=set_return_to_none
    ).grid(row=3, column=0, sticky=tk.W, pady=4)

    tk.Button(
        master,
        text='Submit',
        command=master.quit     # Close the window but don't change the text
    ).grid(row=3, column=1, sticky=tk.W, pady=4)

    master.mainloop()

    return return_val


def backup_object_factory(backup_procedure: str) -> Backup:
    """ This function returns an object which handles the backupprocess."""
    return PROCEDURES[backup_procedure.lower()]


def main():
    """ Main programm starts here"""
    # === Step one ===
    # Setup for argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'procedure',
        help='Specify the procedure type',
        choises=list(PROCEDURES.keys())
    )

    parser.add_argument(
        '-v', '--verbose',
        help='Set the logging output to stdout',
        action='store_true'
    )

    # TODO: Logger needs to be implemented first. Research logging in multiple files and classes
    # parser.add_argument(
    #     '-log',
    #     help='Specify the logging level'
    # )

    args = parser.parse_args()

    # Setup for logger
    # TODO: Implement logger

    # Setup Tkinter
    root = tk.Tk()
    root.withdraw()

    # === Step two ===
    source_path = tk.filedialog.askdirectory(parent=root, title='Select a source directory')
    destination_path = tk.filedialog.askdirectory(parent=root, title='Select a destination directory')
    file_types = None

    if args.procedure == list(PROCEDURES.keys())[1]:
        file_types = _get_userinput_filetypes()     # FIXME: Let this be handled by an object

    # === Step three ===
    backup_instance: Backup = backup_object_factory(args.procedure)
    backup_instance.set_source(source_path)
    backup_instance.set_destination(destination_path)

    if args.procedure == list(PROCEDURES.keys())[1]:
        backup_instance.set_file_types(file_types)

    try:
        backup_instance.backup()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
