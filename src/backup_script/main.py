#!/usr/bin/env python
""" Automatically backup files

Created on: 27.01.2021
@author: Max Weise
"""


import argparse

# def backup_object_factory(backup_procedure: str) -> Backup:
#     """ This function returns an object which handles the backupprocess."""
#     if backup_procedure not in _BACKUP_STRATEGIES.keys():
#         raise KeyError(f'There is no {backup_procedure} Strategie defined')
#
#     return _BACKUP_STRATEGIES[backup_procedure]


def _argument_parser_setup() -> argparse.ArgumentParser:
    """ Defines CLI arguments.

    Returns:
        argparse.ArgumentParser: Namespace for CLI arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'procedure',
        help='Specify the type of backup procedure'
    )

    # parser.add_argument(
    #     '-v', '--verbose',
    #     help='Set the logging output to stdout',
    #     action='store_true'
    # )

    # parser.add_argument(
    #     '-log',
    #     help='Specify the logging level',
    #     choices=list(_LOGGING_LEVELS.keys()),
    #     default=_DEFAULT_LOG_LEVEL
    # )

    return parser.parse_args()


# def _logger_setup(verbose: bool) -> logging.Logger:
#     """ Create the logger for this module."""
#     logger = logging.getLogger('main_script')
#     try:
#         logger.setLevel(_LOGGING_LEVELS[__logging_level])
#     except Exception as e:
#         print(e)
#
#     # Setup file logging
#     file_handler = logging.FileHandler(_LOG_FILE)
#     file_handler.setLevel(logging.DEBUG)
#     log_format = logging.Formatter(_LOG_FORMAT_LOGFILE)
#     file_handler.setFormatter(log_format)
#     logger.addHandler(file_handler)
#
#     # Setup sysout logging (if specified)
#     if verbose:
#         console_handler = logging.StreamHandler(sys.stdout)
#         console_handler.setLevel(_LOGGING_LEVELS[__logging_level])
#         print_format = logging.Formatter(_LOG_FORMAT_CONSOLE)
#         console_handler.setFormatter(print_format)
#         logger.addHandler(console_handler)
#
#     return logger


def main():
    """ Main programm starts here"""
    # Setup argparser and logger
    # args = _argument_parser_setup()
    # logger = _logger_setup(args.verbose, args.log)
    pass


if __name__ == '__main__':
    main()
