""" Class to backup specified filetypes

Created: 01.05.2021
Last revision: 28.05.2021
@author: Max Weise
"""

from shutil import copy
from os import listdir, walk, path

from src.file_backup import File_Backup
# from src.custom_exceptions import Root_Not_Found

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
        """ Get the contents of the __file_types attribute."""
        return self.__file_types

#    def __find_start_directory(self, path_on_system: str, root_to_find: str):
#        """ Find the root directory in a given path.
#            If root doesn't exist in path, a ValueError is raised by the index method."""
#        p_o_sys = path_on_system.split('\\')
#        return p_o_sys.index(root_to_find)
        
    def __check_for_relevant_files(self, list_to_check: list) -> list:
        """ Search a given list of files for files with relevant filetypes."""
        return_list = []
        for f in list_to_check:
            if f.split('.')[-1] in self.__file_types:
                return_list.append(f)

        return return_list
            

    def backup_file_types(self) -> None:
        """ Copy specified files matching the sorting-criterium from root to destination."""
        for root, dirs, files in walk(self.root):
            if len(files) > 0:
                for f in self.__check_for_relevant_files(files):
                    copy(path.join(root, f), self.dest)



