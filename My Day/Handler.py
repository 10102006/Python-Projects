
"""
  Overview>

Classes required:
  1. 

"""

# @ Imports
from ntpath import join
import os
from os import path

import json

from datetime import datetime, time

database_path = path.join("E:\Coding\Python Codes\Projects\My Day\Database")

# * Defining


class Database:
    def __init__(self, path):
        """
          So this functions makes a class a constructor
        """
        self.databasePath = join(path)
        os.chdir(path)

    def CreateSlot(self, name, startingTime, endingTime=''):
        """
        """
        startingTime = time(
            startingTime[0], startingTime[1]) if type(startingTime) == tuple else startingTime
        endingTime = time(
            endingTime[0], endingTime[1]) if type(endingTime) == tuple else endingTime

        slot = {
            "Name": name,
            "StartingTime": startingTime,
            "EndingTime": time(
                startingTime.hour + 1, startingTime.minute) if not endingTime else endingTime,
            "Index": 0,
        }

        Database.SetIndex(slot)
        return slot

    @staticmethod
    def SaveSlot(slot):
        """
        """
        filename = f"{slot['Index']}.json"

        if not path.isfile(filename):
            with open(filename, "w") as file_obj:
                json.dump(slot, file_obj, indent=4, default=str)

    @staticmethod
    def LoadSlot(filename):
        """
        """
        with open(filename, "r") as file_obj:
            return json.load(file_obj)

    @staticmethod
    def SetIndex(slot):
        """ Working """
        for index, file in enumerate(os.listdir(), start=1):
            file = Database.LoadSlot(file)

            startingTime = datetime.strptime(
                file.get("StartingTime"), "%H:%M:%S").time()

            if slot["StartingTime"] < startingTime:
                slot["Index"] = index
                return
        else:
            slot["Index"] = (len(os.listdir()) + 1)

    def AdjustSlot(self, newSlot, index):
        """
        """
        slots = []
        for slot in os.listdir():
            slots.append(self.LoadSlot(slot))
            os.remove(slot)

        slots.insert(index - 1, newSlot)

        for slotIndex, slot in enumerate(slots, start=1):
            slot["Index"] = slotIndex
            self.SaveSlot(slot)


# ? Implementation
if __name__ == "__main__":
    database = Database(database_path)

    slot = database.CreateSlot("Jogging", (12, 32))

    # for index in range(5):
    #     slot = database.CreateSlot(f"Task-{index}", (10 + index * 2, 0))
    #     database.SaveSlot(slot)

    # database.SetIndex()
    database.AdjustSlot(slot, slot["Index"])
