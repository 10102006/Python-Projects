'''
    # Summary

Defination:
      This file will make a folder tree that will be storeded in a list

Tasks:
      1. Listing all the directories


ex:
      Main Folder:
            -sub-folder
               --sub_SubFolder
               --sub_SubFolder
            -sub-folder
               --sub_SubFolder
            -sub-folder
               --sub_SubFolder
               --sub_SubFolder
               --sub_SubFolder

'''

# * Imports
import os
from os import path

rootdir = "C:/Users/udit kumar/Desktop/Coding & Bowsers/Python Codes/Projects/_Notes Apps/Database"
# @ Defining


def PrintFolderTree(f_path, file_folder_only=0, file=[], folder=[]):
    """
        This a recursive method so this will repeat itself

      Things done:
             1. First looping though all the dir in the path
             2. Making a path with the dir name
             3. If the dir is a folder then we will recurse again but with the path that we defined earlier
             4. If the dir is a file then we will print the dir with extension of choice
             5. For cleaing we are index the level of folder heritage

    """
    folder_listDir = os.listdir(f_path)

    for dir in folder_listDir:
        otherpath = path.join(f_path, dir)

        if path.isfile(otherpath):
            file.append(dir)
            os.chdir(rootdir)

        else:
            os.chdir(otherpath)

            folder.append(dir)
            PrintFolderTree(otherpath, file_folder_only, file, folder)

    if file_folder_only == 0:
        return(file)
    elif file_folder_only == 1:
        return(folder)
    else:
        return(file, folder)
