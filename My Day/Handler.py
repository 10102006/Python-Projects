
# @ Imports
from ntpath import join
import os
from os import path

import json

from datetime import datetime, time

database_path = path.join(
    "E:\Coding\Python Development\Projects\My Day\Database")

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
            - Using a certain mechanic for finding time
            - And filling in the values given as param in a dict
            - Finding the index using the ```Database.SetIndex()``` method
            - Returning the dict object formed
        """
        # - In a concatinated way finding if the time values are in a tuple or time format and taking according actions
        # - If the param is tuple then making a time obj using the tuple values
        # - Else using the time obj as it is
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
    def SaveSlot(slotObject):
        """Saving a json file with the index of the slot and storing the data in it"""
        filename = f"{slotObject['Index']}.json"

        if not path.isfile(filename):
            with open(filename, "w") as file_obj:
                # - Using json dump to save the slotObject data
                json.dump(slotObject, file_obj, indent=4, default=str)

    @staticmethod
    def LoadSlot(filename):
        """Retrieving the data store in a specific file"""
        filename = filename if ".json" in filename else f"{filename}.json"

        with open(filename, "r") as file_obj:
            # - Using json load for retrieiving the data
            slot = json.load(file_obj)
            slot.update({timePeriod: datetime.strptime(slot[timePeriod], "%H:%M:%S").time(
            ) for timePeriod in ["StartingTime", "EndingTime"]})

            return slot

    @staticmethod
    def SetIndex(slotObject):
        """
            - Looping through all the files/slots in the database dir
                - Checking if the ```StartingTime``` of the ```slotObject``` is greater than the current iterating file/slot
                - if yes then return the index of the iteration

            - else if the for loop return empty then returning the number of files present in the database, meaning the last index
        """

        # - Looping using enumerate for index counting
        for index, file in enumerate(os.listdir(), start=1):
            file = Database.LoadSlot(file)

            startingTime = file.get("StartingTime")

            # Checking mechanism
            if slotObject["StartingTime"] < startingTime:
                slotObject["Index"] = index
                return
        else:
            # - returning the last index
            slotObject["Index"] = (len(os.listdir()) + 1)

    def AdjustSlot(self, slotObject):
        """
            - Storing all the data of the slots in a list
            - Add the new ```slotObject``` in the list at a certain index
            - Remaking the files in the correct order
        """
        slots = []
        index = slotObject["Index"]

        # - Loading and Appending the slot data into the slots list
        #  - removing the file for further ease
        for slot in os.listdir():
            slots.append(self.LoadSlot(slot))
            os.remove(slot)

        slots.insert(index - 1, slotObject)

        # - Remaking the files in the correct order
        for slotIndex, slot in enumerate(slots, start=1):
            slot["Index"] = slotIndex
            self.SaveSlot(slot)


# ? Implementation
if __name__ == "__main__":
    database = Database(database_path)

    # Single unique slot
    slot = database.CreateSlot("Jogging", (12, 32))

    # Saving the unique slot
    database.SaveSlot(slot)

    # Retrieving the Saved slot
    slot = database.LoadSlot(slot["Index"])

    # Placeholder slots
    for index in range(5):
        slot = database.CreateSlot(f"Task-{index}", (10 + index * 2, 0))
        database.SaveSlot(slot)

    # Rearranging the slots to accomodate the new slot
    database.AdjustSlot(slot)
