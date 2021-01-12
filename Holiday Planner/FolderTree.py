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

# @ Defining


def FolderTree(f_path, rootdir=os.getcwd(), file_folder_only=0, current_path_only=False, file=[], folder=[]):
    """
        This a recursive method so this will repeat itself

      Things done:
             1. First looping though all the dir in the path
             2. Making a path with the dir name
             3. If the dir is a folder then we will recurse again but with the path that we defined earlier
             4. If the dir is a file then we will print the dir with extension of choice
             5. For cleaing we are index the level of folder heritage

    """
    f_path = path.join(f_path)
    folder_listDir = os.listdir(f_path)

    for dir in folder_listDir:
        otherpath = path.join(f_path, dir)

        if path.isfile(otherpath):
            file.append(dir)
            os.chdir(rootdir)

        elif not current_path_only:
            os.chdir(otherpath)

            folder.append(dir)
            FolderTree(otherpath, rootdir=rootdir,file_folder_only=file_folder_only, file=file, folder=folder)

    os.chdir(rootdir)
    if file_folder_only == 0:
        return(file)
    elif file_folder_only == 1:
        return(os.listdir(f_path))
    else:
        return(file, folder)


if __name__ == "__main__":
    t = FolderTree(input('Enter your path: '), 3)
    print(t)
