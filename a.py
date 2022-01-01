from datetime import date, datetime

Task = {
    "Name": "Udit",
    "Done": False,
}

# print(Task)
# Task.__setitem__("Done", True)
# print(Task)

lst = [1, 2, 3, ]
lst.append(5)

[print(item, end=' | ') for item in lst]
print('Yo')
