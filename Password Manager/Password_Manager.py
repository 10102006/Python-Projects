"""
    Summary

"""

# * Imports
from cryptography.fernet import Fernet
import os
import FolderTree

rootdir = 'C:/Users/udit kumar/Desktop/Coding & Bowsers/Python Codes/Projects/Password Manager/Database'

os.chdir(rootdir)

# @ Defining


class Encrypter_Decrypter:
    """
    This class will take care of all the Encryption and Decrypting of the passwords
    What is done:
        1. Generate_key to make a secret key to use as a reference and storing it in a file
        2. Load_key to load the previous key from the file
        3.
    """

    @staticmethod
    def Generate_Key():
        """
        This is one time function which we will run in the starting to make a key which will be use to encrypt and decrypt the passwords
            What is done:
                1. Changing the dir so the key is made in the database dir
                2. key => is most important because this is used to decrypt and encrypt the messages
                3. Then we are opening the a file to store this key in that file
        """

        key = Fernet.generate_key()

        # ? Here we are make a file key is a special extension for encrypted passwords and 'wb' is the special file mode for this key extension type

        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def Load_Scrt_Key():
        """
            Here we are opening the file where the secret key is made and obtaining that key
        """

        # ? Here we are opening the special file, 'rb' is a special mode for key extension
        return open("secret.key", "rb").read()

    def Encrypt_Message(self, message):
        """
            What is done:
                1. Using the Load_Scrt_Key() method to get the key and storing the key
                2. Encoding the message in a certain format with the Fernet module to encrypt it
                3. The using the Fernet module for encrypting the message
                4. Returning the encrypted message
        """
        # @ Storing the previous secret key
        key = self.Load_Scrt_Key()

        # @ Encoding the message using the message module from fernet
        encoded_message = message.encode()

        # ? Here we are encrypting the message/password
        fernet_key = Fernet(key)
        encrypted_message = fernet_key.encrypt(encoded_message)

        return encrypted_message

    def Decrypt_Message(self, encrypted_message):
        """
            What is done:
                1. Loading the secret key from the file using the Load_Scrt_key()
                2. Using the Fernet to decrypt the message
                3. Returning the decrpyted message
        """
        # @ Storing the previous secret key
        key = self.Load_Scrt_Key()

        # ? Here we are decrypting the message/password
        fernet_key = Fernet(key)
        decrypted_message = fernet_key.decrypt(encrypted_message)

        return decrypted_message.decode()


# @ Intialising the Cryptographer Class
Cryptographer = Encrypter_Decrypter()


def MasterPasswordLog(password=''):
    """
    Here were are making a master password which will be used as a set of protection protocol

      What to do:
        1. Taking input if password is not already set in the params
        2. Encypting the password and storing it in a var
        3. Making file with the website name and writing the encrypted password

    """
    # ? This is for checking if the file is already made or not
    if not os.path.isfile('Master_password.key'):
        password = input(
            'Enter your Master Password:  ') if password else password

        # ? Encyrpting the password and storing it in a var
        en_user_password = Cryptographer.Encrypt_Message(password)

        # ? Storing the master password in a file
        with open('Master_password.key', 'wb') as master_password:
            master_password.write(en_user_password)


def Load_Password(filename='', dec_password=''):
    """
    This will load the encrypted password from database file and return the decrypted password

      What to do:
        1. Checking if filename is provided or not if not then taking filename as input
        2. Opeing a try execpt else function for error handling
        3. Storing the encrypted text from the file from the database

    """
    for i in range(10):
        filename = f"{input('Enter your file name: ')}.key" if filename == '' else f"{filename}.key"

        try:
            en_password = open(filename, 'rb').read()
            dec_password = Cryptographer.Decrypt_Message(en_password)
        except:
            if i != 0 and i != 9:
                print('Sorry the file is not available!')
                print('------------------------------------------')
            elif i == 9:
                print('Sorry try again!')
        else:
            return dec_password


def Access_Password(shouldAccess=False):
    """
    This function is a type of authenticater this will take input from the user which will be the master password this will repeat untill the user gets the correct password
      What is done:
         1. First of all we are loading the master password using the Load_Password( method as storing it
         2. Working in a while true loop
            1. Taking input from the in each iteration
            2. Checking if the input is the stored master password or not
            3. If yes then we will break out of the loop continuing the program
            4. Making sure that we want to run the program or not we will make a fail safe which is the should access if this is true then we will continue the program else  we won't
            5.If the is wrong then printing that the input is wrong as continuing the loop

    """
    # ? Retrieving the master password and storing it
    master_password = Load_Password('Master_password')

    # * ALl the functionaly is done inside this
    while True:
        # @ Taking input from the user
        user_pass = input('Enter you master password: ')

        # * Checking the if the input is correct or not
        if user_pass == master_password:

            # @ Make the should acces true
            shouldAccess = True
            print('------------------------------------------')
            break
        else:
            print('Sorry wrong password! \n')

    # ? Returning this var so that it can be stored in a var
    return shouldAccess


def Log_Password(filename='', password=''):
    """
    This the mechanism I will be using to store the passwords with username

    Args:
        filename (str): This represents the website name.
        password (str): This is string password which will be encrypted.

    What is done:
        1. Taking input for both filename and password if it is not predefined
        2. Then we will try to avoid any error
        3. Main
            1. Encrypting the password and storing it
            2. Checking if the file is made or not
            3. If made:
                1. Simply writing inside the file
            4. If not made:
                1. If file name is taken then printing the that file name is taken
                2. Then printing the password if the user wants to
                3. The confirming to overwrite or not
    """

    # ? Taking inputs if they are not pre-defined
    filename = input('Enter file name: ') if not filename else filename
    password = input('Enter your password: ') if not password else password

    # * Main Statement for error handeling
    try:
        # ? Encrypting the password and storing it
        en_password = Cryptographer.Encrypt_Message(password)

        # * Checking if the is already made or not
        if not (os.path.isfile(f'{filename}.key')):

            # * Fail-safe checking if the filename is empty
            if filename != '':

                # ? Finally making the file and writing the encrpted password in it
                with open(f"{filename}.key", 'wb') as t_file:
                    t_file.write(en_password)

        # * If the file is made then telling it to the user and asking to override it or not
        else:
            print('------------------------------------------')
            print('This Password is already taken do you want to override it.')

            # * This is for checking if user know master password
            Access_Password()
            print(Load_Password(filename))

            # * This is confirming logic
            if True if input('Enter 1 to confirm: ') == '1' else False:
                with open(f"{filename}.key", 'wb') as t_file:
                    t_file.write(en_password)
            print('------------------------------------------')

    # * This will only run if the file is not made or some error occurs
    except:
        print('Your password is not saved!')

    # * This is succes message for the user if the file is made and everything is fine
    else:
        print('Password saved successfully!')


def Load_Passwords(pre_folder=[]):
    """
    This is a type of selecting passwords preview which will first display the password then it will ask which password should we open
      What to do:
        1. Using the folder tree py file we will be getting the list of all the files in the database folder
        2. Then we must remove the master password and the secret key from this list to make it a little secure
        3. Printing the elements of the above fromed list with an index
        4. Then we will be changing the dir to database dir for error handling of the opening folder
        5. Asking input of which folder to open
        6. Intialising the name of the file to open,by splicing the .key extension
        7. Using the LoadPassword() loading and storing the password
        8. Printing the password
    """

    # ? Using the folderTree file to get the list of file available in the database folder and storing this list
    pre_folder = FolderTree.PrintFolderTree(
        rootdir) if pre_folder == [] else pre_folder

    if 'Master_password.key' in pre_folder:
        # * Removing the master password and secret key from this list
        pre_folder.remove('Master_password.key')
        pre_folder.remove('secret.key')

    # * Looping through all the elements in thep prev-list and printing them with index
    for index, f_password in enumerate(pre_folder, 1):
        str_file = str(index) + ') ' + f_password[:-4]
        print(str_file)

    # @ Changing the root dir just in case
    os.chdir(rootdir)

    # * This is for error handling
    try:
        # ? Asking for file number
        n_password_f = int(
            input('Enter the file number you want to open: ')) - 1

        # ? Getting the element with index and removing the .key extension and storing
        f_name_password = pre_folder[n_password_f][:-4]

        # ? Storing the return from the Load_Password
        f_password = Load_Password(f_name_password)
    except:
        f_password = 'Sorry wrong input try again!'

    # @ Printing the return password
    print(f_password)
    return pre_folder


def MainLoop():
    """
      What is done:
         1.
    """
    to_access = Access_Password()
    f_passwords = []

    if to_access:
        while True:
            what_todo = True if int(input(
                'What do you want to do(0 for storing and 1 for retireving): ')) == 0 else False

            if what_todo:
                Log_Password()
            else:
                f_passwords = Load_Passwords(f_passwords)


# ? Execution


if __name__ == "__main__":
    MainLoop()
