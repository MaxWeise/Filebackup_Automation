""" Lib to backup the LaTeX tree
    Only keep files of type tex, sty, txt, toc, (pdf)

Created: 15.02.2021
Last revision: 17.02.2021
@author: Max Weise
"""

import os
import shutil

from os import getcwd, mkdir, path, rename
from distutils.dir_util import copy_tree

class File_Backup(object):
    """ Backup all files / directories in specified root dir to a specified destination
        
        @params 
            root: str - root directory
            destination: str - copy to destination

        @author 
            Max Weise
    """
    def __init__(self, root: str, destination: str):
        self.root = root
        self.dest = destination

    def backup_tree(self):
        copy_tree(self.root, self.dest)

    def __str__(self):
        return f'Backing up {self.root} into {self.dest}'
        
class Filetype_backup(File_Backup):
    """ Can be used to backup files with user specific filetypes
        
        @params 
            root: str -  rootdirectory 
            file_types: list -  filetypes to backup

        @author 
            Max Weise
    """ 
    def __init__(self, root: str, destination: str,  file_types: list):
        super().__init__(root, destination)
        self.file_list = file_types
        self.dump_dir = path.join(root, 'auxiliary_files')
    
    def get_dump_dir(self) -> str:
        return self.dump_dir
    
    def dump_files(self):
        try:
            mkdir(self.dump_dir)
        except FileExistsError:
            print(f'The directory does allready exist\n')
        except Exception as e:
            print(e)

        for root, _, files in os.walk(self.root):   # underscore '_' replaces iteration variable 'dir'
            for name in files:
                if name[-3:] not in self.file_list:
                    shutil.move(path.join(root, name), self.dump_dir)
    # override
    def __str__(self):
        return f'Backing up {self.root} into {self.dest} using these filetypes: {self.file_list}'

class Garbage_Collector(object):
    """ Remove the dump directory created by Filetype_Backup
        
        @params 
            O: object - Filebackup object creating a dump directory
        
        @author 
            Max Weise
    """
    def __init__(self, O: File_Backup):
        self.dump_dir = O.get_dump_dir()

    def collect_garbage(self):
        shutil.rmtree(self.dump_dir)

    def __str__(self):
        return f'Cleaning up {self.dump_dir}'

def test():
    # Test code here
    pass

if __name__ == '__main__':
    test()