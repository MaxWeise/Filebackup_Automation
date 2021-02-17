"""
Automatically backup files


Created on: 27.01.2021
Last revision: 17.02.2021
@author: Max Weise
"""

from file_backup_classes import File_Backup, Filetype_backup, Garbage_Collector


def main():
    while (descition := input('>>> ')).lower() != 'x':
        if descition == 'file backup':
            # Copy full tree of src to dst
            src = input('Please provide a source path:\n>>> ')
            dst = input('Please provide a destination path:\n>>> ')

            o = File_Backup(src, dst)
            print(o)
            o.backup_tree()
        elif descition == 'file type backup':
            # Copy specific files from scr to dst
            src = input('Please provide a source path:\n>>> ')
            dst = input('Please provide a destination path:\n>>> ')
            fltyp = input('Please provide a list of filetypes (only letters, no "."):\n>>> ')

            o = Filetype_backup(src, dst, fltyp)
            g = Garbage_Collector(o)
            print(o)
            o.dump_files()
            print(g)
            g.collect_garbage
            o.backup_tree()

        else:
            print(f'ERROR: I dont know the command {descition}, please try again\n')


if __name__ == '__main__':
    main()