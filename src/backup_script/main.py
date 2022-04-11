#!/usr/bin/env python
""" Automatically backup files

Created on: 27.01.2021
@author: Max Weise
"""


import argparse
import logging

import backup_script.backup_strategies.simple_backup_strategy as sbs
import backup_script.backup_strategies.abstract_backup_strategy as ab
import backup_script.backup_strategies.file_type_backup_strategy as fts


STRATEGIES = {
    'simple-backup': sbs.SimpleBackupStrategy(),
    'file-type-backup': fts.FileTypeBackupStrategy()
}


def backup_object_factory(backup_procedure: str) -> ab.Backup:
    """Returns an instance of a concrete backup strategy implementation.

    Args:
        backup_procedure (str): Specifies the strategy to be created.

    Raises:
        KeyError: If the argument passed to the function does not match any
            specified backup strategy.

    Returns:
        ab.Backup: An instance of a concrete implementation of Backup.
    """
    if backup_procedure not in STRATEGIES.keys():
        raise KeyError(f'There is no {backup_procedure} Strategie defined')

    return STRATEGIES[backup_procedure]


def _argument_parser_setup() -> argparse.ArgumentParser:
    """ Defines CLI arguments.

    Returns:
        argparse.ArgumentParser: Namespace for CLI arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'procedure',
        help='Specify the type of backup procedure',
        choices=STRATEGIES.keys()
    )

    parser.add_argument(
        '-v', '--verbose',
        help='Set the logging level to info (default is warning)',
        action='store_true'
    )

    return parser.parse_args()


def _logger_setup(verbose: bool) -> logging.Logger:
    """ Creates a logger for the module.

    Args:
        verbose (bool): Sets the logging level to info if true. If not, level
            is set to false.

    Returns:
        Logger: Module level logger.
    """

    logger = logging.getLogger('backup_logger')
    logger.setLevel(logging.INFO if verbose else logging.WARNING)
    frmt = logging.Formatter('[%(levelname)s] - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(frmt)
    logger.addHandler(console_handler)

    return logger


def main():
    """ Main programm starts here"""
    # Setup argparser and logger
    # args = _argument_parser_setup()
    # logger = _logger_setup(args.verbose, args.log)
    pass


if __name__ == '__main__':
    main()
