""" Automatically backup files

Created on: 27.01.2021
Last revision: 25.02.2021
@author: Max Weise
"""

from file_backup_classes import File_Backup, Filetype_Backup


def main():
    while (descition := input('>>> ')).lower() != 'x':
        if descition == 'file backup':
            # Copy full tree of src to dst
            src = input('Please provide a source path:\n>>> ')
            dst = input('Please provide a destination path:\n>>> ')

            File_Backup_Instance = File_Backup(src, dst)
            print(File_Backup_Instance)
            File_Backup_Instance.backup_tree()
        elif descition == 'file type backup':
            # Copy specific files from scr to dst
            src = input('Please provide a source path:\n>>> ')
            dst = input('Please provide a destination path:\n>>> ')
            fltyp = input('Please provide a list of filetypes (only letters, no "."):\n>>> ')

            ftype_backup = Filetype_Backup(src, dst, fltyp)
            ftype_backup.dump_files()

            if input(f'Confirm deleting {g.dump_dir} (Y/N):\n>>> ') == 'Y':
                ftype_backup.garbage_collector.collect_garbage()
                ftype_backup.backup_tree()
            else:
                pass # safe necessary data and continue as usual
            
            print(f'The directory {ftype_backup.root} has not been copied')
            # Save location to backup later
        else:
            print(f'ERROR: I dont know the command {descition}, please try again\n')

def test():
    pass

if __name__ == '__main__':
    # main()
    test()
