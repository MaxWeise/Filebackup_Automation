""" Automatically backup files
    This module can be used with a gui

Created on: 07.03.2021
Last Revision: 08.03.2021
@author: Max Weise
"""

from user_interface import GUI
from file_backup_classes import File_Backup, Filetype_Backup 

def main():
    app = GUI()
    app.run()
    user_settings = app.get_program_params()

    print(f'Initializing {user_settings[2]}')
    if user_settings[2] == 'File Backup':
        #FIXME Backup won't start
        f_backup = File_Backup(user_settings[0], user_settings[1])
        f_backup.backup_tree()
    elif user_settings[2] == 'File Type Backup':
        user_input = input('Please provide a list of filetypes (no ".")\n>>> ')
        file_list = user_input.split(' ')
        ft_backup = Filetype_Backup(user_settings[0], user_settings[1], file_list)
        ft_backup.dump_files()
        ft_backup.backup_tree()

        if (user := input('Remove unwanted files? (y/n)\n>>> ')) == 'y':
            ft_backup.garbage_collector.collect_garbage()
        else:
            pass # TODO: JSON Safe

if __name__ == '__main__':
    main()