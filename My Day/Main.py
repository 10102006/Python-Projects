"""
  Overview>

"""

# @ Imports
import os
from os import path
import typer

from Handler import Database
import Viewer

database_path = path.join("E:\Coding\Python Codes\Projects\My Day\Database")

# * Defining

# ? Implementation
if __name__ == "__main__":
    database = Database(database_path)
