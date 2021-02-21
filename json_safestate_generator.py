""" Create JSON safelogs to keep track of paths not being backed up or cleaned

Created on: 18.02.2021
Last revision: 18.02.2021
@author: Max Weise
"""
from datetime import date
from os import getcwd, mkdir, path

class JSON_File_Manager(object):
    """ Manage JSON safelogs to determine which paths had a aborted backup
        
        @params
        @author
            Max Weise
    """
    """ Path to directory"""
    def __init__(self):
#        self.root = root # ? Whatfor
        self.__date_of_creation = date.today()
        self.__safe_path = path.join(getcwd(), 'json_safe_logs')  # Remember FileExistsError

    # Getter
    def get_date_of_creation(self):
        return self.__date_of_creation

    def get_safe_path(self):
        return self.__safe_path

    
    def safe_to_json(self):
        dict = {
            'date' : self.get_date_of_creation(),
            'path' : self.get_safe_path(),
            # Reason for json safe
        }
        # JSON dump
        # Return json string, pass to filesafe method

    def load_from_json(self):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    pass
