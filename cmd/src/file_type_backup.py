""" Class to backup specified filetypes

Created: 01.05.2021
Last revision: 01.05.2021
@author: Max Weise
"""

from file_backup_classes import File_Backup

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
    pass
