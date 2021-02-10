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

class CMD():
    """
    """
    pass

# ? Implementation
if __name__ == "__main__":
    pass
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
