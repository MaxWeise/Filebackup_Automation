""" Automatically backup files
    This module can be used with a gui

Created on: 07.03.2021
Last Revision: 10.03.2021
@author: Max Weise
"""

from json_safestate_generator import JSON_File_Manager
from file_backup_classes import File_Backup, Filetype_Backup 
from user_interface import GUI, Yes_No_Interface, Text_Input_Interface

from os import path, listdir, remove

def main():
    # TODO: Recover from json safe
    app = GUI()
    app.run()
    user_settings = app.get_program_params()

    print(f'Initializing {user_settings[2]}')
    if user_settings[2] == 'File Backup':
        f_backup = File_Backup(user_settings[0], user_settings[1])
        print(f_backup)
        f_backup.backup_tree()
    elif user_settings[2] == 'File Type Backup':
        usr_interface = Text_Input_Interface('Provide filetypes')
        usr_interface.run()
        file_list = (usr_interface.get_textbox_content()).split(' ')
        file_list[-1] = (file_list[-1])[:-1]    #* Used to get rid of line break which gets inserted by textbox
        ft_backup = Filetype_Backup(user_settings[0], user_settings[1], file_list)
        ft_backup.dump_files()
        ft_backup.backup_tree()

        conf = Yes_No_Interface(title='Backup Procedure', header='Confirm deleting unwanted files?')
        conf.run()
        if conf.get_confirmation_value():
            ft_backup.garbage_collector.collect_garbage()
        else:
            pass # TODO: JSON Safe
if __name__ == '__main__':
    main()
