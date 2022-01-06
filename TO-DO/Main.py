"""
  Overview>

"""

# @ Imports
import typer
import os
from Database import Database, TaskId
from Viewer import Table, Display

database_path = "E:\Coding\Python Codes\Projects\\TO-DO\Database"

# * Defining

titles = ["Id", "Name", "Priority", "Completed", "Description"]

app = typer.Typer()

database = Database(database_path)
Id = TaskId(database_path)
id = iter(Id)

toDoTable = Table(titles)
display = Display(toDoTable)
Tasks = []


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


@app.command()
def add(taskname: str, priority: int = 0, description: str = ''):
    """
    used for adding tasks
    """
    try:
        task = Task(taskname, next(id), priority, description)
        database.SaveFile(task)

        print(taskname, "made succesfully!")

    except:
        print('error')


@app.command()
def view():
    """
    this is for viewing the task at hand
    """
    pass

    for task in os.listdir(database.database_path):
        if "Task-" in task:
            index = int(task.split('-')[1].split('.')[0])

            task = database.LoadFile(index)

            Tasks.append(task)

    for task in Tasks:
        toDoTable.AddToTable(task)

    display.PrintTable()


@app.command()
def completed(taskid: int):
    """
    for marking the completed tasks
    """
    database.ChangeFile(taskid)
    pass


@app.command()
def remove(taskid: int):
    """
    to remove a certain task using id of the task
    """
    if database.LoadFile(taskid)["Completed"] == True:
        database.TrashFile(taskid)
    else:
        print("Task Not completed!")


@app.command()
def clear(confirmation: bool = False):
    """
    to clear all the task in the list
    """
    canBeCleared = True

    for task in os.listdir(database.database_path):
        if "Task-" in task:
            index = int(task.split('-')[1].split('.')[0])

            task = database.LoadFile(index)

            if task["Completed"] == False:
                canBeCleared = False

            Tasks.append(task)

    if canBeCleared or confirmation:
        for task in Tasks:
            database.TrashFile(task["Id"])
    else:
        print("Cannot clear, task are incompleted, or needs confirmation")


@app.command()
def check(times: int):
    "used for checking the program"
    for index in range(times):
        print("Check", "." * index)
    print("Working!")


# ? Implementation
if __name__ == "__main__":

    app()

    # * - test for save the tasks
    # Tasks = [
    #     Task(name=f"{index}-task",
    #          id=next(id),
    #          priority=2,
    #          description=f"Test task {index}") for index in range(5)
    # ]

    # for task in Tasks:
    #     database.SaveFile(task)

    # * - test for retrieving the tasks
    # for task in os.listdir(database.database_path):
    #     if "Task-" in task:
    #         index = int(task.split('-')[1].split('.')[0])

    #         task = database.LoadFile(index)
    #         Tasks.append(task)

    # * - test for changing the tasks
    # database.ChangeFile(1)

    # * - test for trashing the tasks
    # database.TrashFile(1)

    # for task in os.listdir(database.database_path):
    #     if "Task-" in task:
    #         index = int(task.split('-')[1].split('.')[0])

    #         task = database.LoadFile(index)
    #         Tasks.append(task)

    # [print(task) for task in Tasks]

    # * - test for table formation
    # for task in Tasks:
    #     toDoTable.AddToTable(task)

    # display.PrintTable()
