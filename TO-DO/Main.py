"""
  Overview>

"""

# @ Imports
import typer
from  Database import Database
import Viewer

database_path = "E:\Coding\Python Codes\Projects\\TO-DO\Database"

# * Defining
def Task(name, id, priority=5, description=None):
    description = description if description else name

    task = {
        "Id": id,
        "Name": name,
        "Priority": priority,
        "Completed": False,
        "Description": description
    }

    return task

# ? Implementation
if __name__ == "__main__":
   pass