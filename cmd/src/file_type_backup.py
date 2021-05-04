""" Class to backup specified filetypes

Created: 01.05.2021
Last revision: 01.05.2021
@author: Max Weise
"""

from file_backup import File_Backup

class File_Type_Backup(File_Backup):
    """ This class can be used to backup files regarding 
        their types (file endings '.xxx'). 
        It sorts out all unwanted files and copys the remaining 
        files to the specified backup destination.

        @params
            root: str - root directory
            destination: str - destination directory
            file_types: list - filetyes to backup

        @author
            Max Weise

    """

    def __init__(self, root, destination, file_types):
        """ Initialize object by giving it root, destination and file types to copy."""
        super().__init__(root, destination)
        self.file_types = file_types

    def set_file_types(self, new_file_types: list) -> None:
        """ Set the attribute file_types to a specified list. Mostly used for testing."""
        self.file_types = new_file_types

    def file_type_backup(self) -> None:
        """ Copy specified files matching the sorting-criterium from root to destination."""
        pass