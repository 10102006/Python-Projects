"""Currently working on a back function"""


# * Imports
import os
from os import path
import re

schoolBooks_directory = "E:\\School Stuffs\\School Books"
lightNovels_directory = "F:\\Downloads\\Books"

# @ Defination


def Choose_From_List(list_object):
    """
    This function will be used to choose an item from the {list_object} in the console
        1. Printing all the items with decoration for reference
        2. Taking the input from the user of which item to choose with its index
        3. Returning the item asked => string
    """
    [print(f"{index}. {item}") for index, item in enumerate(list_object, 1)]

    item_wanted = input("Enter the index number of the item you want: ")

    if len(item_wanted) and item_wanted.isnumeric():
        item_wanted = int(item_wanted) - 1
        return list_object[item_wanted]

    elif item_wanted == '.':
        return "."

    else:
        slt_lst = re.findall("[0-9][0-9]|[0-9]", item_wanted)
        slt_lst = [int(item) - 1 for item in slt_lst]

        return slt_lst

    print('-----------------------------------------')


def Previous_path(give_path):
    """
    This function will take all the components from the path and remove the last path
    """
    path_components = re.split("\\\\", give_path)[:-1]

    new_path = ""
    for str in path_components:
        new_path = (f"{new_path}{str}\\\\")

    return new_path


def Main(folder_directory):
    """
    This is the main function where all the stuff is happening
        1. Changing directory to {folder_directory} for check
        2. In a while True:
            1. We will be choosing what item of the current folder we want to choose
            2. Joining the this extension to the {folder_directory}
            3. This loop continue till a file is selected
            4. If another folder is selected we will change the directory to that folder
    """
    os.chdir(folder_directory)

    while True:
        directory_extension = Choose_From_List(os.listdir())


        if type(directory_extension) == list and path.isdir(folder_directory):
            for file in directory_extension:
                print(f"Opening... {os.listdir()[file]}")
                # print(os.listdir()[file])
                temp_folder_directory = path.join(
                    folder_directory, os.listdir()[file])

                # print(temp_folder_directory)

                os.startfile(temp_folder_directory)
            break

        elif directory_extension == ".":
            print("previous selected!")
            folder_directory = Previous_path(folder_directory)
            print(folder_directory)

        else:
            folder_directory = path.join(
                folder_directory, directory_extension)

            if path.isfile(folder_directory):
                print(f"Opening... {directory_extension}")
                os.startfile(folder_directory)
                break

            elif path.isdir(folder_directory):
                os.chdir(folder_directory)


# ? Running the code


if __name__ == "__main__":
    choose_list = ["Light Novels", "School Books", "Own Folder"]
    whatToOpen = Choose_From_List(choose_list)

    if whatToOpen == "Light Novels":
        Main(lightNovels_directory)
    elif whatToOpen == "School Books":
        Main(schoolBooks_directory)
    else:
        new_directory = path.join(input("Enter Path: "))
        Main(new_directory)
