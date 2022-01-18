"""
  Overview>

"""

# @ Imports

from datetime import datetime

from os import path
from ntpath import join


database_path = join("E:\Coding\Python Codes\Projects\My Day\Database")

# * Defining
Slots = [
    {
        "Index": 1,
        "Name": "Task-0",
        "StartingTime": "10:00:00",
        "EndingTime": "11:00:00",
    },
    {
        "Index": 2,
        "Name": "Task-0",
        "StartingTime": "13:00:00",
        "EndingTime": "13:30:00",
    },
    {
        "Index": 3,
        "Name": "Task-0",
        "StartingTime": "20:00:00",
        "EndingTime": "22:00:00",
    }
]


class Schedule:
    def __init__(self, path, slots):
        """
            So this functions makes a class a constructor
        """
        self.databasePath = path
        self.slots = slots
        self.schedule = {f"{key}": [] for key in slots[0].keys()}

    def MakeSchedule(self):
        """
        """
        for slot in self.slots:
            for item in slot:
                self.schedule[item].append(slot[item])

        return self.schedule

    @staticmethod
    def PrintSchedule(schedule):
        """
        """
        [print(key, end=" | ") if key != "Name" else None for key in schedule]
        print("Name...")

        print('-' * 43)

        for index, item in enumerate(schedule["Index"]):
            print(str(item).rjust(4), end=". | ")
            print((schedule["StartingTime"][index]).center(12), end=' - ')
            print((schedule["StartingTime"][index]).center(10), end=' | ')
            print(schedule["Name"][index])


# ? Implementation
if __name__ == "__main__":
    scheduleManager = Schedule(database_path, Slots)

    schedule = scheduleManager.MakeSchedule()
    scheduleManager.PrintSchedule(schedule)
