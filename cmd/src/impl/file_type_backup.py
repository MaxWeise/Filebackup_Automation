""" Class to backup specified filetypes

Created: 01.05.2021
Last revision: 01.05.2021
@author: Max Weise
"""

from os import listdir
from file_backup import File_Backup

class File_Type_Backup(File_Backup):
    """ This class can be used to backup files regarding 
        their types (file endings '.xxx'). 
        It sorts out all unwanted files and copys the remaining 
        files to the specified backup destination.

        @params
            root: str - root directory
            destination: str - destination directory
            __file_types: list - filetyes to backup

        @author
            Max Weise

    """

    def __init__(self, root, destination, __file_types):
        """ Initialize object by giving it root, destination and file types to copy."""
        super().__init__(root, destination)
        self.__file_types = __file_types

    def set__file_types(self, new_file_types: list) -> None:
        """ Set the attribute __file_types to a specified list. Mostly used for testing."""
        self.__file_types = new_file_types

    def get__file_types(self) -> list:
        return self.__file_types

    def backup_file_types(self) -> None:
        """ Copy specified files matching the sorting-criterium from root to destination."""
        all_files = listdir(self.root)
        wanted_files = []

        # Search the files that should be copied
        for f in all_files:
            f_extention = f.split('.')
            if f_extention[-1] in self.__file_types:
                wanted_files.append(f)
        