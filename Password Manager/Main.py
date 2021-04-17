
# * Imports
from cryptography.fernet import Fernet

import os
from os import path

import stdiomask

database_directory = "E:\Coding & Bowsers\Python Codes\Projects\Password Manager\Database"

# @ Defining


def FolderDetails(folder_path, file_extensions=False):
    """
    This a recursive method so this will repeat itself

    Things done:
        1. First looping though all the dir in the path
        2. Making a path with the dir name
        3. If the dir is a folder then we will recurse again but with the path that we defined earlier
        4. If the dir is a file then we will print the dir with extension of choice
        5. For cleaing we are index the level of folder heritage
    """
    folder_listDir = os.listdir(folder_path)
    files = []

    for dir in folder_listDir:
        dir_path = path.join(folder_path, dir)

        if path.isfile(dir_path):
            files.append(dir)

    if not file_extensions:
        files = [file.rsplit(".")[0] for file in files]

        return files


class Crypter():
    """
    """

    @staticmethod
    def GenerateMainKey():
        """
        This is one time function which we will run in the starting to make a key which will be used to encrypt and decrypt the passwords.
            What is done:
                1. Changing the dir so the key is made in the database dir
                2. key => is most important because this is used to decrypt and encrypt the messages
                3. Then we are opening the a file to store this key in that file
        """

        key = Fernet.generate_key()

        with open("main_encryption_key.key", "wb") as key_file:
            key_file.write(key)

    @staticmethod
    def LoadMainKey():
        """
            Here we are opening the file where the secret key is made and obtaining that key
        """

        # ? Here we are opening the special file, 'rb' is a special mode for key extension
        return open("main_encryption_key.key", "rb").read()

    def EncryptPassword(self, given_password):
        """
            What is done:
                1. Using the Load_Scrt_Key() method to get the key and storing the key
                2. Encoding the message in a certain format with the Fernet module to encrypt it
                3. The using the Fernet module for encrypting the message
                4. Returning the encrypted message
        """
        # @ Storing the previous secret key
        key = self.LoadMainKey()

        # @ Encoding the message using the message module from fernet
        encoded_message = given_password.encode()

        # ? Here we are encrypting the message/password
        fernet_key = Fernet(key)
        encrypted_message = fernet_key.encrypt(encoded_message)

        return encrypted_message

    def DecryptPassword(self, encrypted_password):
        """
            What is done:
                1. Loading the secret key from the file using the Load_Scrt_key()
                2. Using the Fernet to decrypt the message
                3. Returning the decrpyted message
        """
        # @ Storing the previous secret key
        key = self.LoadMainKey()

        # ? Here we are decrypting the message/password
        fernet_key = Fernet(key)
        decrypted_message = fernet_key.decrypt(encrypted_password)

        return decrypted_message.decode()


class Password_Manager(Crypter):
    """
    """

    def __init__(self, database_directory):
        """
            So this functions makes a class a constructor
        """
        super().__init__()
        self.database_directory = database_directory
        os.chdir(database_directory)

    def MasterPassword(self, master_password):
        """
        """
        self
        if not os.path.isfile('Master_password.key'):
            encrypted_master_password = super().EncryptPassword(given_password=master_password)

            with open('Master_password.key', 'wb') as master_password:
                master_password.write(encrypted_master_password)

    def SavePassword(self, filename, password, canOveride=False):
        """
        """
        filename = f"{filename}.key" if ".key" in filename else filename

        try:
            encrypted_password = super().EncryptPassword(password)

            if not (os.path.isfile(filename)):
                with open(f"{filename}.key", 'wb') as password_file:
                    password_file.write(encrypted_password)

            else:
                print(
                    'This password-filename is already taken do you want to override it.')

                if (True if input("Enter (1-Yes) (2-No): ") == "1" else False) and canOveride:
                    print(self.LoadPassword(filename))

                    if True if input('Enter 1 to confirm: ') == '1' else False:
                        with open(f"{filename}.key", 'wb') as password_file:
                            password_file.write(encrypted_password)
                            print('Password saved successfully!')

        except Exception as exception:
            print('-----------------------------------------')
            print(exception)
            print('Your password is not saved!')

    def LoadPassword(self, filename='', decrypted_password=''):
        """
        This function will be used to retrieve the passwords
        """
        self
        filename = filename if '.key' in filename else f"{filename}.key"

        try:
            en_password = open(filename, 'rb').read()
            decrypted_password = super().DecryptPassword(en_password)

        except Exception as e:
            print(e)

        else:
            return decrypted_password


class CommandLine_Password_Manager(Password_Manager):
    """
    """

    def __init__(self, datbase_directory):
        """
            So this functions makes a class a constructor
        """
        self.database_directory = datbase_directory
        super().__init__(datbase_directory)

    def MakePassword(self):
        """
        """
        self
        password_filename = input("Enter password filename: ")
        password = stdiomask.getpass()
        try:
            super().SavePassword(password_filename, password)
        except:
            print('-----------------------------------------')
            print("Filename taken!")
            password_filename = input("Enter password filename: ")
            super().SavePassword(password_filename, password)

    def AccessPassword(self, number_trys=3):
        """
        """
        self
        master_password = super().LoadPassword('Master_password')

        while True:
            if number_trys == 0:
                return False

            user_input = stdiomask.getpass(prompt="Enter Master Password: ")

            if user_input == master_password:
                print('-----------------------------------------')
                return True

            number_trys -= 1

    def LoadPasswords(self, password_filenames=[]):
        """
        """
        if password_filenames == []:
            password_filenames = FolderDetails(
                self.database_directory)

        if 'Master_password' in password_filenames or 'main_encryption_key' in password_filenames:
            # * Removing the master password and secret key from this list
            password_filenames.remove('Master_password')
            password_filenames.remove('main_encryption_key')

        for index, password_filename in enumerate(password_filenames, 1):
            decorated_filename = f"{index})  {password_filename}"
            print(decorated_filename)

        os.chdir(database_directory)

        try:
            password_filename_index = int(
                input('Enter the file number you want to open: ')) - 1

            password_filename = password_filenames[password_filename_index]

            decrypted_password = super().LoadPassword(password_filename)
            print('-----------------------------------------')

        except:
            print('Sorry wrong input try again!')
            return None

        else:
            print(password_filename + ' : ' + decrypted_password)
            return decrypted_password, FolderDetails(
                self.database_directory)

    def MainLoop(self):
        """
        What is done:
            1.
        """
        if self.AccessPassword():
            while True:
                what_todo = input(
                    'What do you want to do (1 for storing and 2 for retireving): ')

                if what_todo == "1":
                    what_todo = True
                elif what_todo == "2":
                    what_todo = False

                if what_todo:
                    self.MakePassword()
                elif not what_todo:
                    self.LoadPasswords(password_filenames=[])

                print('-----------------------------------------')


# ? Execution


if __name__ == "__main__":
    pass
    # crypt = Cryptographer()
    # password = "10102119"

    # encypt_password = crypt.EncryptPassword(password)
    # print(encypt_password)

    # decrypt_password = crypt.DecryptPassword(encypt_password)
    # print(decrypt_password)

    # password_manager = Password_Manager(database_directory)
    # password_manager.SavePassword("Google", "51252019")
    # print(password_manager.LoadPassword("Aps School id.key"))

    password_manager = CommandLine_Password_Manager(database_directory)
    # # password_manager.LoadPasswords()
    # # print(password_manager.AccessPassword())
    password_manager.MainLoop()
