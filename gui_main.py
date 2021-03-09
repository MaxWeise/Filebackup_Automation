""" Automatically backup files
    This module can be used with a gui

Created on: 07.03.2021
Last Revision: 09.03.2021
@author: Max Weise
"""

from user_interface import GUI, Confirmation_Dialog
from json_safestate_generator import JSON_File_Manager
from file_backup_classes import File_Backup, Filetype_Backup 

def main():
    # TODO: Recover from json safe
    j_manager = JSON_File_Manager()
    list_of_safed_files = [f for f in listdir(j_manager.get_backup_location())]

    if len(list_of_safed_files) != 0:
        confirmation_window = Confirmation_Dialog()
        if confirmation_window.get_confirmation_value():
            loaded_safes = []
            for this in list_of_safed_files:
                safestate = j_manager.load_from_json(j_manager.read_file(this))     # get json string and parse it to a python dict
                if safestate['backup procedure'] == 'file type backup':
                    pass    # TODO: Implement file type backup
                elif safestate['backup procedure'] is None:
                    pass    # TODO: Implement file backup
                remove(path.join(j_manager.get_backup_location(), this))            # Remove json file after it was dealt with
    else:
        print('No json files found\n')

    app = GUI()
    app.run()
    user_settings = app.get_program_params()

    print(f'Initializing {user_settings[2]}')
    if user_settings[2] == 'File Backup':
        f_backup = File_Backup(user_settings[0], user_settings[1])
        print(f_backup)
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