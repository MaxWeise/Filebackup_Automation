""" Automatically backup files

Created on: 27.01.2021
Last revision: 31.05.2021
@author: Max Weise
"""

from file_backup import File_Backup
from file_type_backup import File_Type_Backup

PROMT = '>>> '

def main():
    print('-------------------------')
    print('Type\n1: File Backup\n2: File Type Backup\n3: Exit')
    print('-------------------------')

    while (user_in := input(PROMT)) != '3':
        if user_in == '1':
            src = input('Src Path: ' + PROMT)
            dst = input('Dst Path: ' + PROMT)

            f = File_Backup(src, dst)
            f.backup_tree()

        elif user_in == '2':
            src = input('Src Path: ' + PROMT)
            dst = input('Dst Path: ' + PROMT)
            ftp = input('File Types: ' + PROMT)

            f = File_Type_Backup(src, dst, ftp)
            f.backup_file_types()



if __name__ == '__main__':
    main()
