""" Automatically backup files

Created on: 27.01.2021
Last revision: 04.03.2021
@author: Max Weise
"""

from file_backup_classes import File_Backup, Filetype_Backup
from json_safestate_generator import JSON_File_Manager

from os import listdir

def f_file_backup(src=None):
    # Copy full tree of src to dst | Backup full tree without requirements
    if src is None:
        src = input('Please provide a source path:\n>>> ')

    dst = input('Please provide a destination path:\n>>> ')

    File_Backup_Instance = File_Backup(src, dst)
    print(File_Backup_Instance)
    File_Backup_Instance.backup_tree()

def f_ftype_backup(src=None):
    # Copy specific files from scr to dst | Sort out unwanted files, delete them and copy the resulting tree
    if src is None:
        src = input('Please provide a source path:\n>>> ')

    dst = input('Please provide a destination path:\n>>> ')
    fltyp = input('Please provide a list of filetypes (only letters, no "."):\n>>> ')

    ftype_backup = Filetype_Backup(src, dst, fltyp)
    ftype_backup.dump_files()

    if input(f'Confirm deleting  all unwanted files (Y/N):\n>>> ') == 'Y':
        ftype_backup.garbage_collector.collect_garbage()
        ftype_backup.backup_tree()
    else:
        print('Backup initialized. Saving state')
        j_manager = JSON_File_Manager()
        j_manager.set_current_working_path(ftype_backup.root)
        reason = 'User interrupted backup'
        j_manager.write_file(j_manager.safe_to_json(reason))

def main():
    j_manager = JSON_File_Manager()
    # Search for json safe files
    list_of_safed_files = [f for f in listdir(j_manager.get_backup_location())]
    if len(list_of_safed_files) != 0:
        if (user_descition := input('There are directories with aboarted backup procedures. Resume these Procedures? (y/n)\n>>> ')) == 'y':
            loaded_safes = []
            for this in list_of_safed_files:
                j = j_manager.load_from_json(j_manager.read_file(this))
                loaded_safes.append(j)

            for safestate in loaded_safes:
                if safestate['backup procedure'] == 'file type backup':
                    f_ftype_backup(safestate['path'])
                elif safestate['backup procedure'] is None:
                    f_file_backup(safestate['path'])
    else:
        print('No json files found\n')

    # TODO: json cant handle the exception object
    try:
        while (descition := input('>>> ')).lower() != 'x':
            if descition == 'file backup':
                f_file_backup()
            elif descition == 'file type backup':
                f_ftype_backup()
            else:
                print(f'ERROR: I dont know the command {descition}, please try again\n')
    except Exception as e:
        j_manager.write_file(j_manager.safe_to_json(e.__str__(), descition))

    print('-- End of module --')
        

if __name__ == '__main__':
    main()