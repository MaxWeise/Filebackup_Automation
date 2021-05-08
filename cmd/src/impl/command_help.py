""" Formatted table which contains information to the commands used in main.py

Created: 05.03.2021
Last revison: 21.03.2021
@author: Max Weise
"""

from prettytable import PrettyTable     # pip install priettytable

def print_help_table():
    x = PrettyTable()
    x.field_names = ['Command', 'Description']
    x.add_rows(
            [
                ['file backup', 'Recursivly copy a specified root directory to a designated destination directory'],
                ['file type backup', 'In addition to "file backup", give a list of file types which get copied. All other files get deleted'],
                ['help', 'Print this table'],
                ['x', 'End the programm'],
            ]
    )
    x.align = 'l'
    print(x)

# print_help_table()
