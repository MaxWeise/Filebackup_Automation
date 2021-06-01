""" Automatically backup files

Created on: 27.01.2021
Last revision: 31.05.2021
@author: Max Weise
"""

import tkinter

from tkinter import filedialog

from file_backup import File_Backup
from file_type_backup import File_Type_Backup

PROMT = '>>> '

def main():
    print('-------------------------')
    print('Type\n1: File Backup\n2: File Type Backup\n3: Exit')
    print('-------------------------')

    root = tkinter.Tk()

    while (user_in := input(PROMT)).strip() != '3':
        try:
            if user_in == '1':
                src = filedialog.askdirectory(parent=root, title='Choose Source Path')
                dst = filedialog.askdirectory(parent=root, title='Choose Destination Path')
    
                f = File_Backup(src, dst)
                f.backup_tree()
    
            elif user_in == '2':
                src = filedialog.askdirectory(parent=root, title='Choose Source Path')
                dst = filedialog.askdirectory(parent=root, title='Choose Destination Path')
                ftp = input('File Types: ' + PROMT)
    
                f = File_Type_Backup(src, dst, ftp)
                f.backup_file_types()
        except Exception as e:
            print(f'ERROR: {e.__str__()}')

        except KeyboardInterrupt as e:
            print(f'{e.__str__()}')
            break

    print('== Ending Programm ==')


if __name__ == '__main__':
    main()
