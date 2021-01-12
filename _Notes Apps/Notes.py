"""
    Summary

What to do:
    1. Get inside the database
    2. Save a note as a file
    3. Inside the notes we can ADD key-points or REMOVE key-points
    4. Retrieve note for getting the info of the file
    5. Display note for displaying the note-file info
    6. Main loop in which we can make note, read note, add/remove key-points

"""

# * Imports
import os
from os import path
from typing import Counter
import FolderTree

# @ Here I am storing the root and database path
rootdir = os.getcwd()
databasedir = path.join(rootdir, "Projects\_Notes Apps\Database")

# ? Changing to the database path
os.chdir(databasedir)


# @ Defining

Database = {}


def MakeNote(noteName, folder='', notes=[]):
    """
      What to do:
        1. Making a folder if the folder name is specified
        2. Param =>
            1. noteName is the name of the file containing the notes
            2. folder is the name of folder we want to make
            3. We can add notes from the begining if we want to by passing the notes in a array

        3. Making a file inside the database with the given note name
        4. Also we can add some notes in advance like some short ones
    """

  # ? This performing all folder related function is the folder name is specified
    if folder:
        folder_path = path.join(databasedir, folder)
        os.mkdir(folder_path)
        os.chdir(folder_path)

  # ? Here I am making the file inside the folder or the root folder
    with open(f'{noteName}.txt', 'w') as f_note:
        # @ Looping to write all the notes in the file
        for k_note in notes:
            f_note.write('- ' + k_note + '\n')

    return str(noteName)


def EditNote(d_note, folder='', editFunction=True):
    """
      What to do:
        1. This function will basically edit the note that we have made like: adding key note to the file deleting a key note.
        2. Params =>
            1. d_note is the name of the file that we have stored in the database
            2. folder if we have stored the note in a folder then we have to specify it's name
            3. editFunction this decides what will be done adding or deleting if this param is set to default then this function will ask what to perform
        3. Making a note list to store all the notes from the file
        4. Looping through the file to get the notes
        5. Printing all the notes for the user to see and evaluate
        6. Then Checking if the function to perform is chosen or not if not then asking the user to chose
        7. When the user has chosen the function to perform or if the function is predefined
        8. Checking which function to perform
        9. If Adding:
            1. Here we are open the note file and then appending the new note

        10. If Deleting:
            1. First we will delete the note we want to delete from the notes list.
            2. Then confirming to delete the note.
            3. If yes then using the MakeNote() => to overwrite the note. but this time the note to be deleted will not be present.
    """
  # ? Here we are initialising the folder path if it is given then changing the dir to that path then for error print folder not found
    if folder:
        folder_path = path.join(databasedir, folder)
        try:
            os.chdir(folder_path)
        except:
            print('Folder not found!')

  # @ Make a notes copy list
    notes = []

  # @ opening the note file with r+ so we can read and write in file
    with open(d_note + '.txt', 'r+') as f_note:

      # ? This loop will get all the raw data from the file and store each note in the note copy list
        while True:
            k_note = (f_note.readline())[:-1]
            if k_note:
                notes.append(k_note)
            else:
                break

      # ? This loop is for print all the notes for the user to check
        for k_note in notes:
            print(k_note)

        print('-----------------------------------------')

    # $ Make so that only one if else is required
      # @ Editing begins here
        # * Checking if the editFunction is specified or not
        if editFunction == True:
            editFunction = int(
                input('What do you want to do(0 for adding, 1 for deleting and 2 for overwriting): '))

        if editFunction == 0:
            print('You are in Appending mode!')
            k_note = input('What do you want to append:  ')
            f_note.write('- ' + k_note)

        else:
            if editFunction == 1:
                print('You are in Deleting mode!')

                n_note = int(
                    input('Enter the note number you want to delete: ')) - 1
                print(notes[n_note])

                if int(input('Enter 1 to confirm and 0 to decline: ')) == 1:
                    notes.remove(notes[n_note])
                    notes = [k_note[2:] for k_note in notes]

            elif editFunction == 2:
                print('You are in Overwriting mode!')

                n_note = int(
                    input('Enter the note number you want to overwrite: ')) - 1

                print(notes[n_note])
                o_note = input('Enter the new key note: \n')

                if int(input('Enter 1 to confirm and 0 to decline: ')) == 1:
                    notes[n_note] = o_note
                    notes = [o_note if k_note == notes[n_note] else k_note[2:]
                             for k_note in notes]

            MakeNote(d_note, notes=notes)


def MakeNoteInConsole():
    """
      What to do:
        1. Print basic stuff for intialising
        2. Ask for note name and folder name => store them in a var
        3. Loop true
        4. In each loop take an input from the user as a note
        5. If the note is empty then the break out of the loop
        6. Use the MakeNote function to make the file
    """
    # @ This is for confirmation
    input('Hi, To continue making the note press enter: ')

    # ? Gathering the info required for the MakeNote()
    note_name = input('Input the name of the note: ')
    folder_name = input(
        'Input the folder name to make a folder or press enter to skip: ')

    print('------------------------------------------')

    options = []

    # @ Line seperator
    print('Enter the notes ;)')

    # * Here I am loop till there is some text given as input if there is no text then this loop will break
    while True:
        key_note = input('> ')

        # * Appending the key_note or breaking out of the loop
        if key_note:
            options.append(key_note)
        else:
            break

    # @ Using a pre-written function to do my chore
    return MakeNote(note_name, folder_name, options)


def OpenDatabase():
    """
      What to do:
        1. Storing the file gathered from the enhanced foldertree file in this folder
        2. Printing all the file with and index
        3. Getting input from the user for which file to open
        4. Using that number to get the file name from the list
        5. Returning the note name
    """
    files = FolderTree.PrintFolderTree(databasedir)
    for file_index, file in enumerate(files, 1):
        print(f'{file_index})', file)

    f_note_number = int(input('Enter the note number you want to open: '))
    return str(files[f_note_number - 1])[:-4]


def ContinueLoop(functionToPerfom, inputContinue=1):
    """
    What is done:
        1. This is a template that I have copied for easily running the functions
        2. We are Loop indefinately
        3. Taking an input and turning that into bool value with short hand if-else
        4. Checking for the input and doing the function
        5. If we chose not to continue the loop will break
    """
    while True:
        input_tocontinue = True if int(
            input(f'{inputContinue} to continue 0 to end: ')) == inputContinue else False
        if input_tocontinue:
            functionToPerfom()
        else:
            break


def Note():
    """
      What to do:
        1. Chosening what to do make note or open note => start_function
    """
    make_open_note = True if int(input(
        "What do you want to do(0 to make a new note file and 1 to open a previous note: ")) == 0 else False

    if make_open_note:
        f_note_name = MakeNoteInConsole()

    else:
        f_note_name = OpenDatabase()

    ContinueLoop(EditNote(f_note_name))


# ? Execution
if __name__ == "__main__":
    Note()
