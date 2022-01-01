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

titles = ["Id", "Name", "Priority", "Completed"]


class Table:
    def __init__(self, titles, rows=0):
        """
            So this functions makes a class a constructor
        """
        self.titles = titles
        self.rows = rows

        self.values = {}

        for title in self.titles:
            if not self.values.__contains__(title):
                self.values[title] = []

        self.GetValues()

    def GetValues(self):
        return self.values


class Display():
    def __init__(self, table):
        """
            So this functions makes a class a constructor
        """
        self.table = table

    def AddToTable(self, object):
        """
        """
        for item in object.keys():
            if item in self.table.titles:
                value = object.get(item)
                self.table.GetValues().get(item).append(value)
            else:
                self.table.titles.append(item)
                self.table.values[item] = [object.get(item)]

        self.table.rows += 1

    def PrintTable(self):
        """
        """
        print('-' * 48)
        [print(title, end=' | ') for title in self.table.titles]

        print()
        print('-' * 48)

        for _ in range(self.table.rows):
            for index, item in enumerate(self.table.values):
                if item != "Titles" and item != "Rows":
                    # print(table.get(item))
                    print(self.table.values.get(item)[(index-2)], end=' | ')
            print()

        print('-' * 48)


# ? Implementation
if __name__ == "__main__":
    pass
    # toDoTable = Table(titles)
    # display = Display(toDoTable)

    # # print(toDoTable.values)

    # display.AddToTable(task)
    # display.AddToTable(task)
    # display.AddToTable(task)

    # # print(toDoTable.values)

    # display.PrintTable()
