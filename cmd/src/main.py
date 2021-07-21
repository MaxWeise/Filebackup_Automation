""" Automatically backup files

Created on: 27.01.2021
Last revision: 20.07.2021
@author: Max Weise
"""

import tkinter

from tkinter import filedialog
from distutils.dir_util import copy_file

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

            src = filedialog.askdirectory(parent=root, title=__SCR_DIALOG)
            dst = filedialog.askdirectory(parent=root, title=__DST_DIALOG)

            if user_in == '1':
                f = File_Backup(src, dst)

            elif user_in == '2':
                ftp = input('File Types: ' + __PROMT)
                f = File_Type_Backup(src, dst, ftp)

            elif user_in == '3':
                singel_file_src = filedialog.askopenfiles(mode='r', parent=root, title=__FIL_DIALOG)
                singel_file_dst = filedialog.askdirectory(parent=root, title=__DST_DIALOG)
                for f in singel_file_src:
                    copy_file(singel_file_src, singel_file_dst)

            f.backup()

        except Exception as e:
            print(f'ERROR: {e.__str__()}')

        except KeyboardInterrupt as e:
            print(f'{e.__str__()}')
            quit()   # Exit the loop on ctrl-c

    print('== Ending Programm ==')


if __name__ == '__main__':
    main()
