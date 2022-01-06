import os

lst = os.listdir('E:\Coding\Python Codes\Projects\TO-DO\Database')

for item in lst:
    if "Task-" in item:
        print(item.split('-')[1].split('.')[0])
