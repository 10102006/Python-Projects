"""
  Overview>

REPL:
  1. Continuous command input
  2. Command Manager will make string shorts for each function
  3. Command format:
    - 

"""

# @ Imports
import os
from os import path
from cmd import Cmd


from datetime import time

from Handler import Database
from Viewer import Schedule

databasePath = path.join(
    "E:\Coding\Python Development\Projects\My Day\Database")
os.chdir(databasePath)

# * Defining


class MyPrompt(Cmd):
    @staticmethod
    def GetSlots():
        """
        """
        database = Database(databasePath)
        slots = [database.LoadSlot(slot) for slot in os.listdir()]
        return slots

    def do_view(self, args):
        """This command will print the schedule."""
        scheduleManager = Schedule(databasePath, self.GetSlots())

        #  Making a schedule
        schedule = scheduleManager.MakeSchedule()

        # Printing the Schedule
        scheduleManager.PrintSchedule(schedule)

    def do_add(self, args):
        """This command will add a slot to the scheule using the input giving by user."""
        database = Database(os.getcwd())

        name = input("Enter slot name: ")
        startingTime, endingTime = (input(f"Enter slot {item}: ").split('-') for item in ["starting time", "ending time"])

        slot = database.CreateSlot(name, startingTime, endingTime)
        database.AdjustSlot(slot)



    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt(databasePath)
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
