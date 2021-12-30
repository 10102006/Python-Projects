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

path: E:\Coding\Python Codes\Projects\TO-DO\Database
path-II: TO-DO\Database

"""

# @ Imports
import os
from os import path
import json
from datetime import date

# * Defining

class Database:
    def __init__(self, path):
        """
            So this functions makes a class a constructor
        """
        self.database_path = path
        os.chdir(self.database_path)

        self.ID()

    def ID(self, function=0):
        """
        """
        if function == 0:
            if not path.isfile(path.join(self.database_path, "ID.txt")):
                with open("ID.txt", "w") as id_file:
                    id_file.write("1")
        elif function == 1:
            with open("Id.txt", "r") as id_file:
                return int(id_file.readline())

    @staticmethod
    def SaveFile(data):
        filename = f"{date.today()}-{data.get('Id')}"

        with open(f"{filename}.json", "w") as json_file:
            json.dump(data, json_file)

    @staticmethod
    def LoadFile(Id):
        filename = f"{date.today()}-{Id}"

        with open(f"{filename}.json", "r") as json_file:
            data = json.load(json_file)
            return data

    def ChangeFile(self, Id, completed=True):
        """
        """
        data = self.LoadFile(Id)
        data.__setitem__("Completed", completed)

        self.SaveFile(data)

    def RemoveFile(self, Id):
        filename = f"{date.today()}-{Id}.json"
        os.remove(path.join(self.database_path, filename))


class TaskId(Database):
    def __iter__(self):
        self.id = self.ID(1)
        return self

    def __next__(self):
        current_id = self.id

        self.id += 1

        with open("Id.txt", "w") as id_file:
            id_file.write(str(self.id))

        return current_id

    @staticmethod
    def resetId():
        with open("Id.txt", "w") as id_file:
            id_file.write('1')


# ? Implementation
if __name__ == "__main__":
    pass
    # database = Database(database_path)

    # _id = TaskId(database_path)
    # Id = iter(_id)

    # task_test = Task("Studying", 1, "Revise for Maths test tomorrow")

    # database.SaveFile(task_test)

    # print(database.LoadFile(8))
    # database.ChangeFile(8, False)
    # print(database.LoadFile(8))

    # database.RemoveFile(8)
