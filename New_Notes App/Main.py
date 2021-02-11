"""
  Overview>

What to do:
    1. 

Notes template:
    => {
        name: ''
        description:''
        notes:['','']
    }

"""

# @ Imports
import pickle
import os
from os import path

Mpath = 'E:\Coding & Bowsers\Python Codes\Projects//New_Notes App\Database'

# * Defining

class Main():
    """
    """
    @staticmethod
    def MakeList(name, description, notes=[]):
        notes = {'name':name, 'description':description, 'notes':notes}
        return notes

    def EditList(self, list_obj, edit_obj, what_to_edit=3, republish=False):
        """
        If the what_to_edit is:
            1. => name of list
            2. => description of list
            3. => (default) List of notes
        """
        previous_name = list_obj.get('name')
        if what_to_edit==1:
            list_obj.update({'name':edit_obj})
            
        elif what_to_edit==2:
            list_obj.update({'description':edit_obj})
            
        else:
            list_obj.update({'notes':edit_obj})

        if republish:
            os.remove(f'{previous_name}.pkl')
            self.PublishList(list_obj)

    @staticmethod
    def PublishList(list_obj, file_path=''):
        """
        """
        os.chdir(Mpath if not file_path else file_path)
        filename = list_obj.get('name')

        filename = filename if '.pkl' in filename else f'{filename}.pkl'
        try:
            with open(filename, 'wb') as file:
                pickle.dump(list_obj, file)
            print(f'{filename} > sucessfully made')
        except Exception as exception:
            print(exception)
            print(filename)

    @staticmethod
    def RetrieveList(list_name, file_path=''):
        """
        """
        if file_path:
            os.chdir(file_path)

        list_name = list_name if '.pkl' in list_name else f'{list_name}.pkl'
        with open(list_name, 'rb') as file:
            data = pickle.load(file)
            return data

class CMD(Main):
    """
    """
    @staticmethod
    def GenerateList():
        """
        """
        t_list = []
        while True:
            item = input('> ')
            if item:
                t_list.append(item)
            else:
                break
        return t_list

    @staticmethod
    def ChooseItemFromList(given_list):
        """
        """
        for index, item in enumerate(given_list, 1):
            print(f'{index}. {item}')
        item_index = input('Enter index of the item: ')

        if item_index.isnumeric():
            item = given_list[int(item_index) - 1]

            return item

    def MakeList(self):
        """
        """
        name = input('Enter name of list: ')
        description = input("Enter list description: ")
        notes = self.GenerateList()

        list_obj = Main.MakeList(name, description, notes)
        Main.PublishList(list_obj)
        return list_obj

    def EditList(self, database_path):
        """
        """
        os.chdir(database_path)
        lists = os.listdir(database_path)

        list_name = self.ChooseItemFromList(lists)

        print(list_name)

        list_obj = Main.RetrieveList(list_name[:-4])

        what_to_edit = input('What do you what to edit(1:name, 2:description, 3:notes): ')
        print('------------------------------------------')
        if what_to_edit == '3':
            edit_obj = self.GenerateList()
        else:
            edit_obj = input(f'Enter {"name" if what_to_edit == "1" else "description"} of the list: ')

        Main.EditList(list_obj, edit_obj, what_to_edit, True)

# ? Implementation
if __name__ == "__main__":
    pass

    main = Main()
    cmd = CMD()

    # t_list = cmd.MakeList()
    # print(t_list)

    # cmd.EditList(Mpath)
    
    # t_list = MakeList('Test', 'test-I')

    # print(t_list)
    # EditList(t_list, ['test_obj_I', 'test_obj_II'], 3)

    # print(t_list)

    # PublishList(t_list, Mpath)
    # t_list = RetrieveList('Test', Mpath)
    # print(t_list)

    # EditList(t_list, 'Test_name_II', 1, True)

    # t_list = RetrieveList('Test_name_II', Mpath)
    # print(t_list)
