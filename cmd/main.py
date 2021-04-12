""" Automatically backup files

Created on: 27.01.2021
Last revision: 12.04.2021
@author: Max Weise
"""

from command_help import print_help_table

""" Note:
    - Inspect the first arg of command list and descide which method to call
    - if no known command -> trash rest of list
    - else -> following str will be flags for command execution
"""
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

def parse_commands(interface_arguments: str) -> list:
    """Take the input line of a user and separate all words into a list. """
    argument_list = interface_arguments.split(' ')
    if argument_list[-1] == '':     # Ignore empty string at end of list
        argument_list.pop(len(argument_list)-1)

    return argument_list
    
'''
    1. Input commands like Powershell or bash (split on space)
    2. Logg activity using decorators
'''
def main():
    while (user_in := input('>>> ')) != 'exit':
        command_list = parse_commands(user_in)
        print(command_list)
        if command_list[0] == 'backup':
            # TODO: Implement backup
            if '-ft' in command_list:
                print('filetype backup')
                command_list.pop(command_list.index('-ft'))
                print(command_list)
            else:
                print('There has been a mistake, there was no option specified')
            pass
        elif command_list[0] == 'help':
            print_help_table()
        else: 
            print(f'Sorry, I dont know the command <{command_list[0]}>')
            print('Type <help> to get an overview of the commands')

if __name__ == '__main__':
    main()
