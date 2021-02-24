""" Create JSON safelogs to keep track of paths not being backed up or cleaned

Created on: 18.02.2021
Last revision: 24.02.2021
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
    def get_date_of_creation(self):
        return self.__date_of_creation

    def get_current_working_path(self):
        return self.__current_working_path

    def get_backup_location(self):
        return self.__backup_location

    def safe_to_json(self, reason: str) -> str:
        safe_stats = {
            'path' : self.get_current_working_path(),
            'date' : str(self.get_date_of_creation()),
            'reason for aboartion' : reason,
        }

        return json.dumps(safe_stats)

    def load_from_json(self, safed_json_sring: str) -> dict:
        return json.loads(safed_json_sring)

    def write_file(self, json_to_safe: str):
        safe_location = self.get_backup_location()
        name = str(self.get_date_of_creation()) + '_log.json'
        try:
            f = open(path.join(self.__safe_folder_name, name), "w")
            f.write(json_to_safe)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def read_file(self):
        pass
        
    def __str__(self):
        return f'cwd : {self.__current_working_path}'

def test():
    j = JSON_File_Manager(getcwd())
    j.write_file(j.safe_to_json('test_reason'))

if __name__ == '__main__':
    test()
