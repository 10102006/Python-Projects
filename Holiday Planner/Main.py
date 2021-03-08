"""
  SUMMARY

State - fldr
{
    details:'',
    tourist_places :
    {
        tourist_place: - fldr
        {
            description: 'string',
            transports: [list of transports],
            hotels: - fldr
            {
                hotel:[ratings, price_of_stay],
            }
        },
        tourist_place: - fldr
        {
            description: 'string',
            transports: [list of transports],
            hotels: - fldr
            {
                hotel:[ratings, price_of_stay]
            }
        },
    }
}


"""

# * Imports
import os
from os import path
from FolderTree import FolderTree


# @ Defination

class Dict_State():
    """
    This will take care of making the dict and storing it in the database
    Futher this will take care of reinitalising the dict which we retored from the files
    """

    @staticmethod
    def Make_Hotel(name_hotel, ratings_hotel, price_hotel):
        """
        This will make an object that is hotel with it's name and details
        Then we will be returning this object to store it in a var
        """
        t_list = [ratings_hotel, price_hotel]
        return name_hotel, t_list

    @staticmethod
    def Make_TouristPlace(name_touristPlace, description_touristPlace, tranports_avail, should_return_name=False):
        """
        This will also make an object Tourist place which will contains its details in a dict and name
        The details will contain the hotel object in it as "hotels"
        This will be returned to store in a var
        """
        t_dict = {
            'description' : description_touristPlace,
            'transports' : tranports_avail,
            'hotels':{}
        }
        return t_dict if not should_return_name else name_touristPlace, t_dict

    @staticmethod
    def Make_State(main_database, name_state, details):
        """
        This will make a State object which will be storing the tourist_place object
        Moreover function will automatically add the state to the main database given
        """
        t_dict = {'tourist_places' : {}}
        main_database.update({name_state : t_dict})
        main_database.get(name_state).update({'details' : details})
        return t_dict

    @staticmethod
    def Add_Hotel(dict_touristPlace, name_hotel ,dict_hotel):
        """
        This will append the formed hotel object to a tourist_place object formed above
        """
        l_pht = dict_touristPlace.get('hotels')
        l_pht.update({name_hotel:dict_hotel})

        dict_touristPlace.update({'hotels':l_pht})

        return dict_touristPlace

    @staticmethod
    def Add_TouristPlace(state, name_touristPlace, dict_touristPlace):
        """
        This will append the tourist_place obj to the state obj
        and then add the state object will be added to the main dict with the name given
        """
        pr = state.get('tourist_places') if state.get('tourist_places') else {}

        pr.update({name_touristPlace:dict_touristPlace})

        state.update({'tourist_places':pr})
        return state

class File_State():
    """
    What to do:
        1. Make state files
            1. Make a folder tourist places
            2. Run the Make tourist files

        2. Make tourist files
            1. Making the detail files:
                1. description -> text
                2. Transport -> we have to write all the transport available
                    1. we will write in alternative lines
                    2. Meaning we will have one line space for distinction
            2. Making a dir for the hotels
            3. Running the Make hotel files inside that folder

        3. Make hotel files
            1. Make the hotel file with the correspoding name(.keys())
            2. Initialise the hotel details
                1. first line: ratings
                2. Second line break for distinguition
                3. Third line: price

    """

    def __init__(self, rootdir=''):
        """
        This is for intialising the main path which is of the main database folder
        """
        self.rootdir = path.join(rootdir)

    @staticmethod
    def Make_Hotels(hotel_path, dict_hotels):
        """
        What is done:
            1. Changing the path to the path specified of the hotel this is important later when we will use this with the make tourist function
            2. Making list of required things:
                1. File_names or hotel names
                2. Details from each hotel obj eg. [[Ratings, Prices],]
            3. Simulaniously looping through each list to get the correct correspondence
            4. File stuff:
                1. Using fstrings making an appropriate file name
                2. Making the file, with using fileformat of opening as 'w'
                3. Obtaining the details from the list using list splicing
                4. Writining the details of the hotel in the file
        """
        # @ Changing the path corresponding to the location where file must be made
        os.chdir(hotel_path)

        # ? Loop through all the keys() => hotel names, values() => details and storing them simulatniously
        file_names = [name for name in dict_hotels.keys()]
        written_details = [value for value in dict_hotels.values()]

        # * Looping through both the list simulatniously
        for (file_name, details) in zip(file_names, written_details):
            file_name = f'{str(file_name)}.txt'

            # ? Making the file and writng the details in it
            with open(file_name, 'w') as file:
                ratings = f'{details[0]}'
                prices = f'${details[1]}'
                file.write(ratings + '\n')
                file.write(prices)

    def Make_TouristPlace(self, tourist_path, dict_touristPlace):
        """
        What is done:
            1. Changing the path to the specified path for convinices in the state making
            2. Obtaining the details of the tourist place obj
                1. description => getting the description from the tourist dict
                2. transports_avail => storing the transport in a list
                3. hotels => Getting the hotel dict
            3. File stuff:
                1. Making a txt description file, and writing description var
                2. Making a txt transport file, and writing each transport in different lines
                3. Making a folder named hotels if it is not made, and storing the path of this folder
                4. Using the Make_Hotels() => params(*hotels, *hotel_path)
        """
        # @ Changing the dir for conviences
        os.chdir(tourist_path)

        # ? Retrieving the details of the tourist place and storing them
        description = dict_touristPlace.get('description')
        transports_avail = dict_touristPlace.get('transports')
        hotels = dict_touristPlace.get('hotels')

        # @ Making a file => (description.txt) and writing the description str
        with open(f'description.txt', 'w') as file:
            file.write(description)

        # @ Making a file => (transport.txt) and writing the description str
        with open(f'transports.txt', 'w') as file:
            for transport in transports_avail:
                file.write(transport + '\n')

        # ? Storing the path of the hotel folder
        hotels_path = path.join(tourist_path, 'hotels')
        # * Checking is the folder is made or not if not then making the folder
        if not path.isdir(hotels_path):
            os.mkdir('hotels')

        # * Using the Make_Hotels function of this class to make the hotel files
        self.Make_Hotels(hotels_path, hotels)

    def Make_State(self, main_path, dict_state, name_state):
        """
        What is done:
            1. Changing the path to the database
            2. Making a folder with the '{state}' name if the folder is not formed
            3. Following the further function is the folder making is succesfull
            4. Main stuff:
                1. Changing the path to the state folder
                2. Making details file and storing the details from the state dict, and then writing the details var
                2. Making a 'tourist places' folder if the folder is not already made using the path of the tourist place path
                3. Continuing if folder making is successfull
                4. Chaging the path to the tourist place folder
                5. TouristPlaces stuff:
                    1. Obtaining the touristplaces dict which contains all the tourist place
                    2. Using the for list loop obtaining all the tourist place dict, and storing them in this list
                    3. Looping through all the tourist places in the list
                    4. Each tourist places stuff:
                        1. Obtaining the path of for the tourist place
                        2. Making a folder of the tourist place if not made
                        3. If the folder making is succesfull then continuing
                        4. Chaging the path to that folder then using the Make_TouristPlace making the tourist places
                        5. Chainging the path to the main tourist place folder so the each folders of the tourist place is made in the correct place
        """
        name_state = name_state.capitalize()
        main_path = path.join(main_path)
        # @ Changing the path to the specified main database
        os.chdir(main_path)

        # ? Making a path for the state by joining the maindatabase path and state name
        state_path = path.join(main_path, name_state)
        # * Checking if the folder is already made
        if not path.isdir(state_path):
            # @ If not then making the folder
            os.mkdir(name_state)

      # @ Main Stuff
        # * Checking if the state folder making is success or not
        if path.isdir(state_path):
            # ? Chaging the path to the respective path of the state
            os.chdir(state_path)

            # @ Making a details file and then writing the in it the details of the state
            with open('details.txt', 'w') as file:
                # ? Obtaininf the details from the dict state and storing it
                details = dict_state.get('details')
                file.write(details)

            # ? Making a path for the tourist place folder by joining the maindatabase path and "tourist places"
            main_tourist_path = path.join(state_path, 'tourist places')

            # * Checking if the folder is already made or not
            if not path.isdir(main_tourist_path):
                # @ Making the folder named "tourist places"
                os.mkdir('tourist places')

            # * Continuing if the folder making is success
            if path.isdir(main_tourist_path):
                # @ Chaging the path to the main touistplace folder
                os.chdir(main_tourist_path)

                # ? Obtainig the main tourist place dict of the state which contains all the tourisplaces and storing it in a var
                main_tourist_places = dict_state.get('tourist_places')

                # ? Looping through all the tourist places and storing there names
                list_tourist_places = [tourist_place for tourist_place in main_tourist_places.keys()]

                # * Looping through all the names in the tourist place list
                for name_tourist_place in list_tourist_places:
                    # ? Making the path by join the main path and name of the tourist place and storing it in a var
                    each_tourist_path = path.join(main_tourist_path, name_tourist_place)

                    # * Checking if the folder is made or not
                    if not path.isdir(each_tourist_path):
                        # @ Making the folder if not made
                        os.mkdir(name_tourist_place)

                    # * Checking if the folder making is success
                    if path.isdir(each_tourist_path):
                        # @ Chaging the path to the path of the specific tourist place
                        os.chdir(each_tourist_path)

                        # ? Obtaining the tourist place dict from the main tourist place dict
                        dict_tourist_place = main_tourist_places.get(name_tourist_place)

                        # @ Using the Make_TouristPlace function making tourist place stuff in the {tourist place name} folder for current tourist place
                        self.Make_TouristPlace(each_tourist_path, dict_tourist_place)

                        # * Chaging the path to the main tourist place folder for convienences
                        os.chdir(main_tourist_path)

    @staticmethod
    def Retrieve_Hotels(hotel_path):
        """
        What is done:
            1. Making a mock hotel dict
            2. Checking the validity of the path by join
            3. Getting all the file names of the hotel using the FolderTree file and splicing the name for removing the extension
            4. Changing the dir to the hotel path
            5. Looping through all the hotels_names in the list:
                1. Trying to open all current hotel and retieving the data by readline and storing them
                2. Adding the attributes to the premetioned dict_hotel
            6. After all the hotels are added to the dict_hotel then returning the dict_hotel

        """
        # @ Temporary dict storing all the hotel objects
        dict_hotel = {}

        # ? Reassuring that the path is in correct format
        hotel_path = path.join(hotel_path)
# $ There is some error with the FolderTree fix it checking what file list is returned
        # ? Obtaining the file name using the FolderTree file splicing each of the filename so the extension(.txt) is removed
        file_names = [file for file in FolderTree(hotel_path, current_path_only=True, file_folder_only=0)]

        # * Changing the path to the hotel path
        os.chdir(hotel_path)

        # * Looping through all the names in the list prementioned
        for file_name in file_names:
# $ Improve here because the file names list is excessive
            try:
                # * Opening each file with respective name
                with open(str(file_name)) as file:
                    # ? Since the first line is rating and second line is price so they will be consistent
                    # * Also here I am splicing the string obtained so (\n) is removed
                    ratings = file.readline()[:-1]
                    price_of_stay = file.readline()

                    # ? Splicing the filename so (.txt) is removed
                    file_name = file_name[:-4]
                    # @ Making the attributes of the hotel in the hotel
                    dict_hotel.update({file_name:[ratings, price_of_stay]})
            except:
                pass

        return dict_hotel

    def Retrieve_TouristPlace(self, touristplace_path):
        """
        What is done:
            1. Making a mock dict for storing the tourisplaces
            2. Reassuring that the tourist path is vaild
            3. Changing the path to the validated path
            4. Gathering of data:
                1. Opening the description file and storing the data gathered in the {description} var
                2. Gathering the transports:
                    1. Making a mock transport list
                    2. Loop True so that all the transports are took
                    3. First we will readline() => This is like a generator so this will change each line it recalled
                    4. If the data gathered is empty then that means the all the transports are gathered and the loop will break
                    5. Splicing the transport to remove the (\n) from the data
                    6. If not then storing the tranport gathered in the prementioned mock transport list
                3. Gathering the hotels:
                    1. Making path by joining the main tourisplace path and the 'hotel' key word
                    2. Using the RetrieveHotels() method gathering the hotels data => Storing the return dict in a var
            4. After gathering the data we will update the each attribute of and giving them corresponding values
            5. Returning the mock dict
        """
        # @ Mock tourist dict
        dict_tourist = {}

        # ? Validating the path then changing the dir to the path
        touristplace_path = path.join(touristplace_path)
        os.chdir(touristplace_path)

        # @ Getting the desciption => str
        with open('description.txt') as file:
            description = file.read()

        # @ Getting the transports => []
        with open('transports.txt') as file:
            # @ Mock transport list
            transports = []

            # ? While continous loop
            while True:
                # * Using the generator getting all the line
                transport = file.readline()

                # * Checking if the tranport is empty then breaking the loop
                if not transport:
                    break

                # * Otherwise continuing the loop
                else:
                    # ? Storing the transport without the extension
                    transport = transport[:-1]
                    transports.append(transport)

        # ? Making the path for the hotels and then retrieving the hotel dict
        hotel_path = path.join(touristplace_path, 'hotels')
        hotels = self.Retrieve_Hotels(hotel_path)

        # @ Updating all the attributes of the tourist place
        dict_tourist.update({'description':description, 'transports':transports,'hotels':hotels})

        return dict_tourist

    def Retrieve_State(self, main_path, name_state):
        """
        What is done:
            1. 
        """
        # @ Mock dict for the state
        dict_state = {'tourist_places':{}}

        # ? Validating the main database path
        main_path = path.join(main_path)

        # @ Changing the path and also Captialising the name of the state for conviniences
        os.chdir(main_path)
        name_state.capitalize()

        # ? Making the state path by join the main database path and the name of the state and changing dir to that path
        state_path = path.join(main_path, name_state)
        os.chdir(state_path)

        # @ Opening the details file of the state
        with open('details.txt') as file:
            # ? Gathering the details and storing it in a variable
            details = file.read()

            # @ Updatng the state dict for inculding the details
            dict_state.update({'details':details})

        # ? Making a path for the tourist place folder containing all the tourist places obj files
        touristPlaces_path = path.join(state_path, 'tourist places')

        # @ Changing the dir to the tourisplace folder
        os.chdir(touristPlaces_path)

        # ? Obtaining all the folders in the touirst place folder
        list_touristplaces = os.listdir()

        # * Looping through all the folder names in the list pre-formed
        for name_tourist_place in list_touristplaces:
            # ? Making path for the current tourist place
            touristplace_path = path.join(touristPlaces_path, name_tourist_place)

            # ? Retrieving the tourist place using the Retrieve_TouristPlace() =>  to get the dict
            dict_tourist_place = self.Retrieve_TouristPlace(touristplace_path)

            # @ Changing the path to the current tourist place
            os.chdir(touristPlaces_path)

            # ? Updating the state dict for adding the tourist place in the state dict
            dict_state.get('tourist_places').update({name_tourist_place:dict_tourist_place})

        # @ Returing the dict
        return dict_state


class CLI(Dict_State):
    """
    How it should work:

    1. Which state do you want to visit => [list of states]
        1. Print description
        2. Confirm => Using the Recursive Function
    2. Which tourist place do you want to visit => [list of tourist places]
        1. Print description
        2. Confirm
        3. Tell transports => [list of transports]
            1. Confirm
        4. Which hotel do you want to vist => [list of hotel names]
            1. Print Ratings
                1. Confirm
            2. Print Price
                1. Confirm
            3. Confirm
    """

    def __init__(self, main_database):
        self.database = main_database

    def Choose_From_List(self, p_list, placeholder_txt='Which item do you want(enter index no or name): ',symbol='.'):
        """
        """
        m_list = [item for item in p_list]
        for index, item in enumerate(m_list, 1):
            printed_str = (f'{index}{symbol} {item}')
            print(printed_str)

        print('-----------------------------------------------------')
        choosen_item = input(placeholder_txt)
        r_item = ''

        try:
            if choosen_item.isnumeric():
                r_item = m_list[int(choosen_item) - 1]
            elif choosen_item in m_list:
                r_item = choosen_item
        except:
            print('Soory some error!')
            self.Choose_From_List(p_list, placeholder_txt, symbol)
        else:
            print('-----------------------------------------------------')
            print(r_item)
            print('-----------------------------------------------------')

            confirm = True if input('Do you chose above item (Y/N): ').capitalize() == 'Y' else False
            if confirm:
                print('-----------------------------------------------------')
                return r_item
            else:
                self.Choose_From_List(p_list, placeholder_txt, symbol)

            return r_item

    def Main(self, main_database):
        """
        """
        state_name = self.Choose_From_List(main_database.keys())

        state = main_database.get(state_name)
        state_details = state.get('details')

        print('details: ' + state_details)

        main_touristplace = state.get('tourist_places')
        tourist_place_name = self.Choose_From_List(main_touristplace.keys())

        tourist_place = main_touristplace.get(tourist_place_name)
        tourist_place_description = tourist_place.get('description')
        print('Description: ' + tourist_place_description)

        transports_list = tourist_place.get('transports')
        transport = self.Choose_From_List(transports_list)

        main_hotels = tourist_place.get('hotels')
        hotel_name = self.Choose_From_List(main_hotels.keys())

        hotel = main_hotels.get(hotel_name)
        ratings, price = hotel[0], hotel[1]

        print('Ratings of hotel' + str(hotel_name) + 'are: ' + ratings)
        print('Prices of hotel' + str(hotel_name) + 'are: ' + price)

        confirm = True if input('Do you accept the hotel? (Y/N): ').capitalize() == 'Y' else False
        if confirm:
            ticket = self.Make_Ticket(hotel_name, hotel, tourist_place_name, transport, state_name)

            return ticket
        else:
            self.Main(main_database)

    @staticmethod
    def Make_Ticket(name_hotel, hotel, name_tourist_place, transport, name_state):
        """
        width = 94
        hieght = 10
        """
        ticket_obj = {}
        ticket_obj.update({name_state:{}})

        tourist_place = {"transport":transport, name_hotel:hotel}

        t_state = ticket_obj.get(name_state)
        t_state.update({name_tourist_place:tourist_place})

        return ticket_obj

    @staticmethod
    def Print_Ticket(ticket):
        """
        """
        ticket_line = f'{"-" * 90}'

        def print_line(line, line_width=92):
            """
            """
            gap = ' ' * ((line_width - 2) - len(line))
            t_line = '|' + str(line) + gap + '|'
            print(t_line)

        def get_first(lst, sh=False):
            """
            """
            _lst = [item for item in lst]
            return _lst if sh else _lst[0]

        print_line(ticket_line)
        print_line('')

        state = get_first(ticket.keys())
        print_line('    State: ' + state)
        touristplace = get_first(ticket.get(state).keys())
        print_line('    Tourist place: ' + touristplace)

        print_line('')

        # lst =[]

        hotel = get_first(ticket.get(state).get(touristplace).keys(), True).pop(1)
        print_line('    Hotel: ' + hotel)
        transport = ticket.get(state).get(touristplace).get('transport')
        print_line('    Transport: ' + transport)

        print_line('')

        price = ticket.get(state).get(touristplace).get(hotel)[1]
        print_line('    Price: ' + price)
        print_line(ticket_line)

# ? Implementation

if __name__ == "__main__":
    Database = {}

    cli = CLI(Database)
    init = Dict_State()
    file = File_State('E:\Coding & Bowsers\Python Codes\Projects\Holiday Planner\Database')

   # ? Trial
    Karnataka = file.Retrieve_State('E:\Coding & Bowsers\Python Codes\Projects\Holiday Planner\Database', 'Karnataka')
    Maharashtra = file.Retrieve_State('E:\Coding & Bowsers\Python Codes\Projects\Holiday Planner\Database', 'Maharashtra')

    Database.update({'Karnataka':Karnataka, 'Maharashtra' : Maharashtra})

    # ticket = cli.Main(Database)
    # print('---------------------------------------------------------------')

    ticket = cli.Make_Ticket('Hotel*', ['10/10', '$1000'], 'Tourist place*', 'Transport*', 'State*')

    cli.Print_Ticket(ticket)
