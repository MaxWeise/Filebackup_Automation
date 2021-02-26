""" Module to copy a directory recursivly, either everything or only specific filetypes.
    In both cases, the structure of the directory will be keept.

Created: 15.02.2021
Last revision: 26.02.2021
@author: Max Weise
"""

# NOTE: Inner classes is a thing in python. To call method from inner class use outer().Inner().method()

import os
import shutil

from distutils.dir_util import copy_tree
from os import getcwd, mkdir, path, rename

class File_Backup(object):
    """ Backup all files / directories in specified root dir to a specified destination
        
        @params 
            root: str - root directory
            destination: str - copy to destination

        @author 
            Max Weise
    """
    def __init__(self, root: str, destination: str):
        """Initialize File_Backup object by giving it a rootdirectory to copy from and a destination to copy to. """
        self.root = root
        self.dest = destination

    def backup_tree(self) -> None:
        """Copy recursivly from self.root to self.dest. """
        copy_tree(self.root, self.dest)

    def __str__(self) -> str:
        """Print a humanly readable representation to the console. """
        return f'Backing up {self.root} into {self.dest}'
        
class Filetype_Backup(File_Backup):
    """ Can be used to backup files with user specific filetypes
        
        @params 
            root: str -  rootdirectory 
            file_types: list -  filetypes to backup

        @author 
            Max Weise
    """ 
    def __init__(self, root: str, destination: str,  file_types: list):
        """Initialize Filetype_backup object by giving root and dest to superconstructor and specifing a list of filetypes to backup."""
        super().__init__(root, destination)
        self.file_list = file_types
        self.dump_dir = path.join(root, 'auxiliary_files')
        self.garbage_collector = Garbage_Collector(self.dump_dir)
    
    def get_dump_dir(self) -> str:
        """Return the path to dump_dir. """
        return self.dump_dir
    
    def dump_files(self) -> None:
        """Move unwanted filetypes to a directory which later gets deleted by a garbage collector. """
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
    def __str__(self) -> str:
        """Print a humanly readable representation to the console. """
        return f'Backing up {self.root} into {self.dest} using these filetypes: {self.file_list}'

class Garbage_Collector(object):
    """ Remove the dump directory created by Filetype_Backup
        
        @params 
            O: object - Filebackup object creating a dump directory
        
        @author 
            Max Weise
    """
    def __init__(self, dump_dir: str):
        """Initialise a Garbage_collection object by giving a object which produces 'garbage'."""
        self.dump_dir = dump_dir

    def collect_garbage(self) -> None:
        """Remove the dump_dir created by File_Backup object. """
        shutil.rmtree(self.dump_dir)

    def __str__(self) -> str:
        """Print a humanly readable representation to the console. """
        return f'Cleaning up {self.dump_dir}'

def msg():
    print('This module is not suposed to be run as a main module')
    print('To debugg, please run the <test.py> module')


if __name__ == '__main__':
    msg()
