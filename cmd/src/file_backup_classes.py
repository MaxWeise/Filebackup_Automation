""" Module to copy a directory recursivly, either everything or only specific filetypes.
    In both cases, the structure of the directory will be keept.

Created: 15.02.2021
Last revision: 28.04.2021
@author: Max Weise
"""
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
        self.file_types = file_types
    
    # override
    def __str__(self) -> str:
        """Print a humanly readable representation to the console. """
        return f'Backing up {self.root} into {self.dest} using these filetypes: {self.file_types}'

def msg():
    print('This module is not suposed to be run as a main module')
    print('To debugg, please run the <test.py> module')


if __name__ == '__main__':
    msg()
