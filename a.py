from datetime import date, datetime

Task = {
    "Name": "Udit",
    "Done": False,
}

print(Task)
Task.__setitem__("Done", True)
print(Task)
