"""
  Overview>

This is a prototype for the os config of ariel like a side project

What needs to be done:
1. File handling => can make, delete, change file name
2. Folder handling => can make folder, move files to/from the folder, beautify the folder
3. Open apps => from the appdata folder
4. Command handler =>  core for the above functions

"""

# @ Imports
from ntpath import join
import os
from os import path

import re

# * Defining

working_path = r"D:\Coding\Python Codes\Projects\OS handler\Database"


class File:
    # $ Later make it like that it will work using the users path
    def __init__(self, working_path):
        """
            So this functions makes a class a constructor
        """
        self.working_path = working_path
        os.chdir(self.working_path)

        self.pre_defined_paths = [
            "C:\\Users\\uditk\\Desktop",
            "C:\\",
            "D:\\"
        ]

    # $ Use kwagrs** and agrs** to make heirarchyy like this ("filename", "txt", "Test-I", "Test-I_")
    def MakeFile(self, filename, format=''):
        """
        This function will make a file in the current directory;
        """
        filename = filename if not format else f"{filename}.{format}"
        try:
            with open(filename, 'x'):
                pass
        except:
            raise Exception("Error!")
        else:
            print(filename, "made!")
            return

    @staticmethod
    def RenameFile(filename, new_filname):
        """
        """
        try:
            file_path = path.join(working_path, filename)

            format = re.split(r'\.', filename)[1]
            revised_file_path = path.join(
                working_path, f"{new_filname}.{format}")

            if path.exists(file_path):
                os.rename(file_path, revised_file_path)
            else:
                raise Exception("Filename does not exists!")

        except Exception as error:
            print(error)
        else:
            print(f"{filename} renamed to {new_filname}.{format}")
            return revised_file_path

    def DeleteFile(self, filename):
        """
        """
        file_path = path.join(self.working_path, filename)
        if path.exists(file_path):
            try:
                print(file_path)
                conf = input(f"Enter 0 to confirm to delete {filename}: ")

                if conf == '0':
                    os.remove(file_path)
                    print(f"Removed {filename}!")

            except Exception as error:
                print(error)

        else:
            raise Exception("File does not exists!")


class Folder:
    def __init__(self, working_path):
        """
            So this functions makes a class a constructor
        """
        self.working_path = working_path
        os.chdir(self.working_path)

    def MakeFolder(self, folderName):
        """"""
        os.mkdir(join(self.working_path, folderName))
        return join(self.working_path, folderName)


class Handler(File, Folder):
    def __init__(self, working_path):
        """
            So this functions makes a class a constructor
        """
        self.working_path = working_path
        os.chdir(working_path)

    def ResetDirector(self, new_directory):
        """
        """
        self.working_path = new_directory
        os.chdir(self.working_path)

    def MakeFile(self, filename, format='', heirarchy=''):
        """
        """
        if heirarchy:
            try:
                new_working_path = join(self.working_path, heirarchy)
                self.ResetDirector(new_working_path)

                super().MakeFile(filename, format)
            except:
                raise Exception("Heirarchay is wrong")

        else:
            super().MakeFile(filename, format)

        self.ResetDirector(self.working_path)


# ? Implementation
if __name__ == "__main__":
    pass

    handler = Handler(working_path)

    # handler.MakeFile("sameple_5", "txt", "Test-I//")
