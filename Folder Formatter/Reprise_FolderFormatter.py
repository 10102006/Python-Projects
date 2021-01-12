"""
  SUMMARY
What to be done:
    1. Capitalise file names
    2. Make a folder for each format => Special name for folder*
    *** 3. Detailed file for the formatter history
            1. Date formatted
            2. Total number of files

"""

# * Imports
import os
from os import path
from FolderTree import FolderTree

_path = path.join('E:\School Stuffs\Academic\Holiday homework winter')
os.chdir(_path)

# @ Defination
def FormatFilenames(folderpath=_path, shouldNumberised=False):
    """
    """
    folderpath = path.join(folderpath)
    files = FolderTree(folderpath)

    for file in files:
        os.rename(file.capitalize())

    print('----------------------------------------------------------------------')

    if shouldNumberised:
        for index, file in enumerate(files, 1):
            n_filename = f'{index}_{file}'
            os.rename(n_filename)

def ExtractFormats(folderpath=_path):
    """
    """
    folderpath = path.join(folderpath)
    files = FolderTree(folderpath)

    formats = []

    for file in files:
        _, format = file.rsplit('.')
        if format not in formats:
            formats.append(format)

    return formats

# ? Implementation
if __name__ == "__main__":
  FormatFilenames(shouldNumberised=True)