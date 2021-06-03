""" Automatically backup files

Created on: 27.01.2021
Last revision: 31.05.2021
@author: Max Weise
"""

import tkinter

from tkinter import filedialog

from file_backup import File_Backup
from file_type_backup import File_Type_Backup

__PROMT = '>>> '
__SCR_DIALOG = 'Choose Source Path'
__DST_DIALOG = 'Choose Destination Path'
__FIL_DIALOG = 'Choose your file(s)'


def main():
    print('-------------------------')
    print('Type\n1: File Backup\n2: File Type Backup\n3: Pick Specific Files\n4: Exit')
    print('-------------------------')

    root = tkinter.Tk()
    root.withdraw()     # tkinter window won't be shown all the time

    while (user_in := input(__PROMT)).strip() != '4':
        try:
            if user_in == '1':
                src = filedialog.askdirectory(parent=root, title=__SCR_DIALOG)
                dst = filedialog.askdirectory(parent=root, title=__DST_DIALOG)

                f = File_Backup(src, dst)
                f.backup_tree()

            elif user_in == '2':
                src = filedialog.askdirectory(parent=root, title=__SCR_DIALOG)
                dst = filedialog.askdirectory(parent=root, title=__DST_DIALOG)
                ftp = input('File Types: ' + __PROMT)

                f = File_Type_Backup(src, dst, ftp)
                f.backup_file_types()

            elif user_in == '3':
                src = filedialog.askopenfiles(mode='r', parent=root, title=__FIL_DIALOG)
                dst = filedialog.askdirectory(parent=root, title=__DST_DIALOG)
                for f in src:
                    print(f.name)

        except Exception as e:
            print(f'ERROR: {e.__str__()}')

        except KeyboardInterrupt as e:
            print(f'{e.__str__()}')
            break

    print('== Ending Programm ==')


if __name__ == '__main__':
    main()
