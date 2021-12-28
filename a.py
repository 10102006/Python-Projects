import re
from os import path


pt = "E:\\School Stuffs\\School Books"
def Previous_path(give_path):
    """
    """
    path_components = re.split("\\\\", give_path)[:-1]

    new_path = ""
    for str in path_components:
        new_path = (f"{new_path}{str}\\")

    return new_path

print(pt)
print(Previous_path(pt))