""" Create JSON safelogs to keep track of paths not being backed up or cleaned

Created on: 18.02.2021
Last revision: 03.03.2021
@author: Max Weise
"""
import json
import datetime

from datetime import date
from os import getcwd, mkdir, path, listdir

class JSON_File_Manager(object):
    """ Manage JSON safelogs to determine which paths had a aborted backup
        
        @params
            current_working_path: str - Path wich had a aborted backup
        @author
            Max Weise
    """
    def __init__(self):
        """Initialise a json_file_manager object and specifing the directory which is currently worked on. """
        self.__safe_folder_name = 'json_safe_logs'
        self.__current_working_path = ''
        date = datetime.datetime.now()
        self.__date_of_creation = str(date)[:10] + '_' + (date.strftime('%X')).replace(':', '-')
        self.__backup_location = path.join(getcwd(), self.__safe_folder_name)
        try:    # Create a directory to story json safe logs
            mkdir(self.__safe_folder_name)
        except FileExistsError:
            print('Backupdirectory allready exists, proceed as normal\n')
        except Exception as e:
            print(e)

    # Getter
    def get_date_of_creation(self) -> date:
        """Return the date of creaton in the format YYYY-MM-DD_HH-MM-SS """
        return self.__date_of_creation

    def get_current_working_path(self) -> str:
        """Return the directory which is currently worked on. """
        return self.__current_working_path

    def get_backup_location(self) -> str:
        """Return the location in which json files get safed. """
        return self.__backup_location
    
    def get_files_in_backup_dir(self) -> list:
        """Return a list of all files in the backupdirectory. """
        return [f for f in listdir(self.get_backup_location()) if path.isfile(path.join(self.get_backup_location(), f))]
    
    # Setter
    def set_current_working_path(self, new_path: str) -> None:
        self.__current_working_path = new_path

    def safe_to_json(self, reason: str, backup_procedure=None) -> str:
        """Collect necessary data and return it as json-string. """
        safe_stats = {
            'path' : self.get_current_working_path(),
            'date' : str(self.get_date_of_creation()),
            'reason for aboartion' : reason,
            'backup procedure' : backup_procedure,
        }

        return json.dumps(safe_stats)

    def load_from_json(self, safed_json_sring: str) -> dict:
        """Convert a json-string and return it as dictionary. """
        return json.loads(safed_json_sring)

    def write_file(self, json_to_safe: str) -> None:
        """Write a given json-string to a json file. """
        safe_location = self.get_backup_location()
        name = str(self.get_date_of_creation()) + '_log.json'
        try:
            with open(path.join(self.__safe_folder_name, name), "w") as f:
                f.write(json_to_safe)
        except Exception as e:
            print(e)

    def read_file(self, file_to_read) -> str:
        """Read a file and return its content as json-string. """
        content = ''
        path_to_file = path.join(self.get_backup_location(), file_to_read)
        try:
            with open(path_to_file, "r") as f:
                content = f.readline()
        except Exception as e:
            print(e)

        return content

    # override
    def __str__(self):
        """Print a humanly readable representation to the console. """
        return f'cwd : {self.__current_working_path}'

def msg():
    print('This module is not suposed to be run as a main module')
    print('To debugg, please run the <test.py> module')


if __name__ == '__main__':
    msg()
