"""

What to do:
  1. Database:
      1. filename => date + id
      {
          "Id": {[id = enumerator]};
          "Name": {string};
          "Priority": {int};
          "Completed": {bool};
          "Description": {string};
      }
      2. task maker
      3. task retriever
      4. task changer
      5. task remover

"""

# @ Imports
import typer
import os
import json
import datetime

# * Defining


class Database:
    def __init__(self, path):
        """
            So this functions makes a class a constructor
        """
        self.database_path = path


class TaskId(Database):

    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        current_id = self.id
        self.id += 1

        return current_id


def Task(name, priority, description=None):
    """
    """
    pass

    description = name

    id = 1

    task = {
        "Id": id,
        "Name": name,
        "Priority": priority,
        "Completed": False,
        "Description": description
    }


# ? Implementation
if __name__ == "__main__":
    pass
