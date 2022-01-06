What all can be done:
   1. init => initialising the home database
   2. list => viewer which will display the to do list

      To-Do List: Date

      ID.   | Name   | Pri | Done | Description
      ----------------------------------------------
      1.    |        |     |      |
      2.    |        |     |      |
      3.    |        |     |      |
      ----------------------------------------------

   3. add(taskName, taskPriority=3, taskDescription=taskName) => this will add tasks to the list
   4. complete(taskId) => this is mark the task as completed
   5. remove(taskId) => this will remvoe the task after confirmation
   6. clear => whole list cleared after confirmation

Database:
   - make an instance of {Database} class => database = Database(database_path)
   - make an id enumerator => Id = TaskId(database_path)
                              id = iter(Id)
   - make a task in dict format
   - save the task using => database.SaveFile(task)
   - retrieve the task using => r_task = database.LoadFile(taskId)
   - #check the task using => database.ChangeFile(taskId)
   - delete the task using => database.TrashFile(taskId)
   - clean Trash folder => database.CleanTrash(True if input("Clean Trash y/n: ") == 'y' else False)

Viewer:
   - make an instance of {Table} class => toDoTable = Table(titles)
   - make an instance of {Display} class => display = Display(toDoTable)
   - add task to the table using => toDoTable.AddToTable(task)
   - print the table using => display.PrintTable()
