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
from os import path, remove
from cmd import Cmd


from datetime import time

from Handler import Database
from Viewer import Schedule

database_path = path.join(
    "E:\Coding\Python Development\Projects\My Day\Database")
os.chdir(database_path)

# * Defining


class MyPrompt(Cmd):
    database = Database(os.getcwd())

    @staticmethod
    def GetSlots():
        """
        """
        database = Database(database_path)
        slots = [database.LoadSlot(slot)
                 for slot in sorted(os.listdir(), key=len)]
        # [print(slot) for slot in slots]
        return slots

    def do_view(self, args):
        """This command will print the schedule."""
        scheduleManager = Schedule(database_path, self.GetSlots())

        #  Making a schedule
        schedule = scheduleManager.MakeSchedule()

        print(schedule)

        # Printing the Schedule
        scheduleManager.PrintSchedule(schedule)

    def do_add(self, args):
        """This command will add a slot to the scheule using the input giving by user."""

        name = input("Enter slot name: ")
        startingTime, endingTime = (input(f"Enter slot {item}: ").split(
            '-') for item in ["starting time", "ending time"])

        slot = self.database.CreateSlot(name, startingTime, endingTime)
        print(slot)
        self.database.AdjustSlot(slot)

    def do_align(self, args):
        """
        """
        slots = self.GetSlots()

        time = sorted([slot["StartingTime"] for slot in slots])

        for slot in slots:
            for index, indexTime in enumerate(time, start=1):
                if slot["StartingTime"] == indexTime:
                    slot.update({"Index": index})

        slots = sorted(slots, key=lambda slot: slot["Index"])

        [remove(slot) for slot in os.listdir()]
        [self.database.AdjustSlot(slot) for slot in slots]

        self.do_view([])

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt(database_path)
    prompt.prompt = '> '
    # prompt.cmdloop('Starting prompt...')
