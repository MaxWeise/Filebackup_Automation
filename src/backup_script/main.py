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
from backup_script.tk_file_extention_dialog import TextInputDialog


def backup_object_factory(backup_procedure: bool) -> Backup:
    """ This function returns an object which handles the backupprocess."""
    if backup_procedure:
        return File_Type_Backup()
    else:
        return File_Backup()


def main():
    """ Main programm starts here"""
    # Setup for argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-ft', '--filetype',
        help='Set the procedure to file type backup',
        action='store_true'
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

    source_path = tk.filedialog.askdirectory(parent=root, title='Select a source directory')
    destination_path = tk.filedialog.askdirectory(parent=root, title='Select a destination directory')
    file_types = None

    if args.filetype:
        text_input_dialog = TextInputDialog('Please enter file extentions')
        text_input_dialog.run()
        file_types = text_input_dialog.get_user_input()

    backup_instance: Backup = backup_object_factory(args.filetype)
    backup_instance.set_source(source_path)
    backup_instance.set_destination(destination_path)

    if args.filetype:
        backup_instance.set_file_types(file_types)

    try:
        backup_instance.backup()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
