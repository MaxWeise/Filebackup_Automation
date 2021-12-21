#!/usr/bin/env python
""" Automatically backup files

Created on: 27.01.2021
@author: Max Weise
"""

import sys
import logging
import argparse
import tkinter as tk
from tkinter import filedialog

from datetime import date

from backup_script.backup import Backup
from backup_script.file_backup import File_Backup
from backup_script.file_type_backup import File_Type_Backup
from backup_script.tk_file_extention_dialog import TextInputDialog

_LOGGING_LEVELS = {
    'debug'     : logging.DEBUG,
    'info'      : logging.INFO,
    'warning'   : logging.WARNING,
    'error'     : logging.ERROR,
    'critical'  : logging.CRITICAL,
}

_LOG_FORMAT_CONSOLE = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
_LOG_FORMAT_LOGFILE = '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s'
_LOG_FILE = f'{date.today()}_logfile.log'

_BACKUP_STRATEGIES = {
    'backup'            : File_Backup(),
    'filetypebackup'    : File_Type_Backup(),
}


def backup_object_factory(backup_procedure: str) -> Backup:
    """ This function returns an object which handles the backupprocess."""
    if backup_procedure not in _BACKUP_STRATEGIES.keys():
        raise KeyError(f'There is no {backup_procedure} Strategie defined')

    return _BACKUP_STRATEGIES[backup_procedure]


def _argument_parser_setup() -> argparse.ArgumentParser:
    """ Define all arguments for the script and return an ArgumentParser instance."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'procedure',
        help='Specify the type of backup procedure'
    )

    parser.add_argument(
        '-v', '--verbose',
        help='Set the logging output to stdout',
        action='store_true'
    )

    parser.add_argument(
        '-log',
        help='Specify the logging level',
        choices=list(_LOGGING_LEVELS.keys()),
        default=_LOGGING_LEVELS['info']
    )

    return parser.parse_args()


def _logger_setup(verbose: bool, __logging_level=logging.DEBUG) -> logging.Logger:
    """ Create the logger for this module."""
    logger = logging.getLogger('main_script')
    logger.setLevel(__logging_level)

    # Setup file logging
    file_handler = logging.FileHandler(_LOG_FILE)
    file_handler.setLevel(logging.INFO)
    log_format = logging.Formatter(_LOG_FORMAT_LOGFILE)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # Setup sysout logging (if specified)
    if verbose:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(__logging_level)
        print_format = logging.Formatter(_LOG_FORMAT_CONSOLE)
        console_handler.setFormatter(print_format)
        logger.addHandler(console_handler)

    return logger


def main():
    """ Main programm starts here"""

    args = _argument_parser_setup()                 # Setup for argparse
    logger = _logger_setup(args.verbose, args.log)  # Setup for logger

    # Setup Tkinter
    root = tk.Tk()
    root.withdraw()

    logger.info('Selecting directories')
    source_path = filedialog.askdirectory(parent=root, title='Select a source directory')
    destination_path = filedialog.askdirectory(parent=root, title='Select a destination directory')
    # file_types = None

    backup_instance: Backup = backup_object_factory(args.procedure)
    logger.info(f'Created {backup_instance}')

    if isinstance(backup_instance, File_Type_Backup):
        logger.debug('is true')
        logger.info('Selecting filetypes')
        text_input_dialog = TextInputDialog('Please enter file extentions')
        try:
            text_input_dialog.run()
        except Exception as e:
            logger.warning(e)

        file_types = text_input_dialog.get_user_input()
        backup_instance.set_file_types(file_types)

        logger.info(f'Selected {file_types}')

    backup_instance.set_source(source_path)
    backup_instance.set_destination(destination_path)
    logger.info(f'Selected {source_path} as source, {destination_path} as destination')

    try:
        backup_instance.backup()
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    main()
