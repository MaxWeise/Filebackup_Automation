""" Automatically backup files

Created on: 27.01.2021
Last revision: 15.04.2021
@author: Max Weise
"""

from command_help import print_help_table
import file_backup_classes as fb

""" Note:
    - Inspect the first arg of command list and descide which method to call
    - if no known command -> trash rest of list
    - else -> following str will be flags for command execution
"""

def parse_commands(interface_arguments: str) -> list:
    """Take the input line of a user and separate all words into a list. """
    argument_list = interface_arguments.split(' ')
    if argument_list[-1] == '':     # Ignore empty string at end of list
        argument_list.pop(len(argument_list)-1)

    return argument_list

def ask_src_dst_paths() -> tuple:
    """Return user-given source and destinaiton paths. """
    user_scr = input('Please provide a source path\n>>> ')
    user_dst = input('Please provide a destination path\n>>> ')
    
    return user_scr, user_dst

def ask_file_types() -> list:
    """Return user-given list of filetypes. """
    f_types = input('Please provide a list filetypes\n>>< ')

    return f_types.split(' ')

'''
    1. Input commands like Powershell or bash (split on space)
    2. Log activity using decorators

    TODO: Python 3.10 -> Switch case for better readability
'''
def main():
    while (user_in := input('>>> ')) != 'exit':
        command_list = parse_commands(user_in)

        if command_list[0] == 'backup':
            command_list.pop(command_list.index('backup'))
            if '-ft' in command_list:
                command_list.pop(command_list.index('-ft'))
                src_dst_tupel = ask_src_dst_paths()
                backup = fb.Filetype_Backup(src_dst_tupel[0], src_dst_tupel[1], ask_file_types())
               # TODO: Implement filetype backup procedure
               #       Simplify FT_Backup class -> files get sorted out directly, delete will be specified by flag
            elif '-f' in command_list:
                command_list.pop(command_list.index('-f')) 
                src_dst_tupel = ask_src_dst_paths()
                backup = fb.File_Backup(src_dst_tupel[0], src_dst_tupel[1])
                print(backup)
                backup.backup_tree()
            else:
                print('There has been a mistake, there was no option specified')

        elif command_list[0] == 'help':
            print_help_table()
        else: 
            print(f'Sorry, I dont know the command <{command_list[0]}>')
            print('Please check the spelling and try again')
            print('Type <help> to get an overview of the commands')

if __name__ == '__main__':
    main()
