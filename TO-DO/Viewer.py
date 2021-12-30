"""
  Overview>

"""

# @ Imports

# * Defining
task = {
    "Id": 5,
    "Name": "Groceries",
    "Priority": 2,
    "Completed": False,
    "Description": "Buy potato and ketchup"
}


class Display():
    def __init__(self, task):
        """
            So this functions makes a class a constructor
        """
        self.task = task

    def MakeTable(self, rows=[], columns=[], cellSize=5):
        """
        What to do:
            1. First make a table dict which will contain all the info about the table
            2. 
        """
        if not rows and not columns:
            rows = self.task.keys()

        table = {
            "Titles": ["Id", "Name", "Done"],
        }

        for title in table.get("Titles"):
            if not table.__contains__(title):
                table[title] = [' ' for column in range(columns)]

        return table

    def PrintTable(self, table):
        """
        """
        print('-----------------------------------------')
        pass

# ? Implementation
if __name__ == "__main__":
    display = Display(task)

    toDoTable = display.MakeTable(4, 5)
    display.PrintTable(toDoTable)
