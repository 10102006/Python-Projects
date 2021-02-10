"""
  Overview

What to do:
    1. Note data type creater => in memory
    2. Note publisher => in Database folder
    3. Note editor => add/remove/overwrite key-note
    4. Print note => specil format of printing

"""

# @ Imports
import os
from os import path
import pickle

# * Defining

Database = {}

database_path = path.join(os.getcwd(), 'Destop Assistant\Database')

def MakeNote(title, content=[]):
  """
  """
  note = {}
  note.update({title:content})

  Database.update({'Notes':[note]})

  return note

def EditNote(note, content):
  """
  """
  content = list(note.values()) + content

  note.update({list(note.keys())[0]:content})
  # return note

def PublishNote(note):
    """
    What is done:
        1. filename confirmation this will add the '.pkl' format if the format is not avail
        2. Then we will make a file with the filename with binary encoding
        3. When the file is made then we will add the data to the file
    """
    os.chdir(database_path)
    
    filename = list(note.keys())[0]
    filename = filename if '.pkl' in filename else f'{filename}.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(list(note.values())[0], file)

def PrintNote(note):
  """
  """
  print(list(note.items())[0])

# ? Implementation
if __name__ == "__main__":
  note = MakeNote(input('Enter note name: '), [10, 'Udit'])
  print(note)

  EditNote(note, [2006, 'Udit'])
  print(note)
  
  PublishNote(note)
  print(os.listdir(database_path))