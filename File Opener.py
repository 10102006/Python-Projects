
# * Imports
import os
from os import path

schoolBooks_directory = "D:\\School Stuffs\\School Books"
lightNovels_directory = "E:\\Downloads\\Books"

# @ Defination

def Choose_From_List(list_object):
    """
    This function will be used to choose an item from the {list_object} in the console
        1. Printing all the items with decoration for reference
        2. Taking the input from the user of which item to choose with its index
        3. Returning the item asked => string
    """
    [print(f"{index}. {item}") for index, item in enumerate(list_object, 1)]

    index_wanted_item = int(
        input("Enter the index number of the item you want: ")) - 1

    print('-----------------------------------------')
    return list_object[index_wanted_item]


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

        folder_directory = path.join(folder_directory, directory_extension)

        if path.isfile(folder_directory):
            print(f"Opening... {directory_extension}")
            break
        elif path.isdir(folder_directory):
            os.chdir(folder_directory)

    os.startfile(folder_directory)

# ? Running the code

if __name__ == "__main__":
    choose_list = ["Light Novels", "School Books"]
    whatToOpen = Choose_From_List(choose_list)

    if whatToOpen == "Light Novels":
        Main(lightNovels_directory)
    elif whatToOpen == "School Books":
        Main(schoolBooks_directory)
