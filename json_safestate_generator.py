""" Create JSON safelogs to keep track of paths not being backed up or cleaned

Created on: 18.02.2021
Last revision: 25.02.2021
@author: Max Weise
"""
import json

from datetime import date
from os import getcwd, mkdir, path

class JSON_File_Manager(object):
    """ Manage JSON safelogs to determine which paths had a aborted backup
        
        @params
            current_working_path: str - Path wich had a aborted backup
        @author
            Max Weise
    """

    def __init__(self, current_working_path):
        """Initialise a json_file_manager object and specifing the directory which is currently worked on. """
        self.__safe_folder_name = 'json_safe_logs'
        self.__current_working_path = current_working_path
        self.__date_of_creation = date.today()
        self.__backup_location = getcwd() + self.__safe_folder_name
        try:    # Create a directory to story json safe logs
            mkdir(self.__safe_folder_name)
        except FileExistsError:
            print('Path allready exists, proceed as normal\n')
        except Exception as e:
            print(e)

    # Getter
    def get_date_of_creation(self) -> date:
        """Return the date of creaton in the format YYYY.MM.DD . """
        return self.__date_of_creation

    def get_current_working_path(self) -> str:
        """Return the directory which is currently worked on. """
        return self.__current_working_path

    def get_backup_location(self) -> str:
        """Retunr the location in which json files get safed. """
        return self.__backup_location

    def safe_to_json(self, reason: str) -> str:
        """Collect necessary data and return it as json-string. """
        safe_stats = {
            'path' : self.get_current_working_path(),
            'date' : str(self.get_date_of_creation()),
            'reason for aboartion' : reason,
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
            f = open(path.join(self.__safe_folder_name, name), "w")
            f.write(json_to_safe)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def read_file(self) -> str:
        """Read a file and return its content as json-string. """
        pass
        
    # override
    def __str__(self):
        """Print a humanly readable representation to the console. """
        return f'cwd : {self.__current_working_path}'

def test():
    pass

if __name__ == '__main__':
    test()
